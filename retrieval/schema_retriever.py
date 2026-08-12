"""
Retrieval layer for the text-to-SQL pipeline.

Instead of dumping the full DB schema into every prompt, we:
1. Introspect the SQLite DB into per-table "schema chunks" (columns, types,
   foreign keys, and a few sample rows).
2. Maintain a small bank of (question -> SQL) few-shot examples.
3. Use TF-IDF cosine similarity (no external embedding API / internet
   required) to retrieve only the chunks/examples relevant to a given
   natural language question.

Swap `TfidfRetriever` for a real embedding-based retriever (e.g. Chroma +
sentence-transformers) later without changing the calling code -- both
expose `.retrieve_schema(question, k)` and `.retrieve_examples(question, k)`.
"""
import sqlite3
from dataclasses import dataclass
from typing import List

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


@dataclass
class SchemaChunk:
    table: str
    text: str


@dataclass
class FewShotExample:
    question: str
    sql: str


# A small seed bank of NL -> SQL examples. In a real system this would grow
# over time (e.g. logging validated queries back into the bank).
FEW_SHOT_BANK: List[FewShotExample] = [
    FewShotExample(
        "How many customers do we have from India?",
        "SELECT COUNT(*) FROM customers WHERE country = 'India';",
    ),
    FewShotExample(
        "What is the total revenue from delivered orders?",
        "SELECT SUM(oi.quantity * oi.unit_price) AS revenue "
        "FROM order_items oi JOIN orders o ON oi.order_id = o.order_id "
        "WHERE o.status = 'delivered';",
    ),
    FewShotExample(
        "List the top 3 products by total quantity sold.",
        "SELECT p.name, SUM(oi.quantity) AS total_qty "
        "FROM order_items oi JOIN products p ON oi.product_id = p.product_id "
        "GROUP BY p.name ORDER BY total_qty DESC LIMIT 3;",
    ),
    FewShotExample(
        "Which customers have never placed an order?",
        "SELECT c.name FROM customers c "
        "LEFT JOIN orders o ON c.customer_id = o.customer_id "
        "WHERE o.order_id IS NULL;",
    ),
]


def build_schema_chunks(db_path: str, sample_rows: int = 2) -> List[SchemaChunk]:
    """Introspects the SQLite DB and returns one text chunk per table."""
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    tables = [
        r[0]
        for r in cur.execute(
            "SELECT name FROM sqlite_master WHERE type='table' "
            "AND name NOT LIKE 'sqlite_%'"
        ).fetchall()
    ]

    chunks = []
    for table in tables:
        cols = cur.execute(f"PRAGMA table_info({table})").fetchall()
        col_desc = ", ".join(f"{c[1]} ({c[2]})" for c in cols)

        fks = cur.execute(f"PRAGMA foreign_key_list({table})").fetchall()
        fk_desc = "; ".join(f"{fk[3]} -> {fk[2]}.{fk[4]}" for fk in fks)

        rows = cur.execute(f"SELECT * FROM {table} LIMIT {sample_rows}").fetchall()
        col_names = [c[1] for c in cols]
        row_desc = " | ".join(str(dict(zip(col_names, r))) for r in rows)

        text = (
            f"Table: {table}\n"
            f"Columns: {col_desc}\n"
            f"Foreign keys: {fk_desc or 'none'}\n"
            f"Sample rows: {row_desc}"
        )
        chunks.append(SchemaChunk(table=table, text=text))

    conn.close()
    return chunks


class TfidfRetriever:
    """TF-IDF based retriever over schema chunks and few-shot examples."""

    def __init__(self, db_path: str, examples: List[FewShotExample] = None):
        self.db_path = db_path
        self.chunks = build_schema_chunks(db_path)
        self.examples = examples if examples is not None else FEW_SHOT_BANK

        self._schema_vectorizer = TfidfVectorizer(stop_words="english")
        self._schema_matrix = self._schema_vectorizer.fit_transform(
            [c.text for c in self.chunks]
        )

        self._example_vectorizer = TfidfVectorizer(stop_words="english")
        self._example_matrix = self._example_vectorizer.fit_transform(
            [e.question for e in self.examples]
        )

    def retrieve_schema(self, question: str, k: int = 3) -> List[SchemaChunk]:
        q_vec = self._schema_vectorizer.transform([question])
        sims = cosine_similarity(q_vec, self._schema_matrix)[0]
        ranked = sorted(
            zip(self.chunks, sims), key=lambda x: x[1], reverse=True
        )
        # Always include at least 1 result even if similarity is low.
        top = [c for c, s in ranked[:k]]
        return top

    def retrieve_examples(self, question: str, k: int = 2) -> List[FewShotExample]:
        if not self.examples:
            return []
        q_vec = self._example_vectorizer.transform([question])
        sims = cosine_similarity(q_vec, self._example_matrix)[0]
        ranked = sorted(
            zip(self.examples, sims), key=lambda x: x[1], reverse=True
        )
        return [e for e, s in ranked[:k]]


if __name__ == "__main__":
    r = TfidfRetriever("db/demo.db")
    q = "How much revenue did we make from delivered orders in June?"
    print("--- Retrieved schema chunks ---")
    for c in r.retrieve_schema(q):
        print(c.text, "\n")
    print("--- Retrieved few-shot examples ---")
    for e in r.retrieve_examples(q):
        print(e.question, "->", e.sql)
