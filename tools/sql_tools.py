"""
Guardrails + execution helpers for running LLM-generated SQL safely
against the demo SQLite database.
"""
import re
import sqlite3
from dataclasses import dataclass
from typing import Any, List, Optional

# Statement types we never allow, regardless of framing.
BLOCKED_KEYWORDS = [
    "DROP", "DELETE", "UPDATE", "INSERT", "ALTER", "TRUNCATE",
    "CREATE", "REPLACE", "ATTACH", "DETACH", "PRAGMA", "VACUUM",
]


@dataclass
class ValidationResult:
    ok: bool
    error: Optional[str] = None


@dataclass
class ExecutionResult:
    ok: bool
    columns: List[str] = None
    rows: List[tuple] = None
    error: Optional[str] = None


def _strip_sql(sql: str) -> str:
    """Removes markdown code fences the LLM sometimes wraps SQL in."""
    sql = sql.strip()
    sql = re.sub(r"^```(sql)?", "", sql, flags=re.IGNORECASE).strip()
    sql = re.sub(r"```$", "", sql).strip()
    return sql


def is_read_only(sql: str) -> bool:
    upper = sql.upper()
    return not any(re.search(rf"\b{kw}\b", upper) for kw in BLOCKED_KEYWORDS)


def validate_sql(db_path: str, sql: str) -> ValidationResult:
    """Guardrail check + dry-run via EXPLAIN (does not execute the query)."""
    sql = _strip_sql(sql)

    if not sql.strip().upper().startswith("SELECT"):
        return ValidationResult(ok=False, error="Only SELECT statements are allowed.")

    if not is_read_only(sql):
        return ValidationResult(
            ok=False,
            error="Query contains a blocked keyword (only read-only SELECT is allowed).",
        )

    try:
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute(f"EXPLAIN {sql}")
        conn.close()
        return ValidationResult(ok=True)
    except sqlite3.Error as e:
        return ValidationResult(ok=False, error=str(e))


def execute_sql(db_path: str, sql: str, row_limit: int = 200) -> ExecutionResult:
    sql = _strip_sql(sql)
    try:
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute(sql)
        columns = [d[0] for d in cur.description] if cur.description else []
        rows = cur.fetchmany(row_limit)
        conn.close()
        return ExecutionResult(ok=True, columns=columns, rows=rows)
    except sqlite3.Error as e:
        return ExecutionResult(ok=False, error=str(e))


if __name__ == "__main__":
    db = "db/demo.db"
    good = "SELECT name, country FROM customers WHERE country = 'India';"
    bad = "DROP TABLE customers;"

    print(validate_sql(db, good))
    print(validate_sql(db, bad))
    print(execute_sql(db, good))
