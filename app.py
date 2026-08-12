"""
Streamlit chat UI for the Text-to-SQL multi-agent pipeline.

Run:
    streamlit run app.py
"""
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
import pandas as pd
from dotenv import load_dotenv

from retrieval.schema_retriever import TfidfRetriever
from agents.crew import run_pipeline

load_dotenv()

DB_PATH = os.path.join(os.path.dirname(__file__), "db", "demo.db")

st.set_page_config(page_title="Text-to-SQL Assistant", page_icon="🗄️", layout="wide")
st.title("🗄️ Text-to-SQL Assistant")
st.caption(
    "Ask a question in plain English. A retrieval-grounded multi-agent "
    "pipeline (Retriever → SQL Generator → Validator → Explainer) turns it "
    "into SQL, runs it, and explains the result."
)

if not os.path.exists(DB_PATH):
    st.error(
        "Demo database not found. Run `python db/setup_demo_db.py` first, "
        "then restart this app."
    )
    st.stop()

if "retriever" not in st.session_state:
    st.session_state.retriever = TfidfRetriever(DB_PATH)

if "history" not in st.session_state:
    st.session_state.history = []

with st.sidebar:
    st.subheader("Demo schema")
    st.caption("customers, products, orders, order_items")
    st.markdown(
        "**Try asking:**\n"
        "- What is the total revenue from delivered orders?\n"
        "- Which customers are from India?\n"
        "- Top 3 products by quantity sold\n"
        "- Which customers have never placed an order?"
    )
    if not os.environ.get("GROQ_API_KEY") and not os.environ.get("OPENAI_API_KEY") and not os.environ.get("ANTHROPIC_API_KEY"):
        st.warning("No LLM API key detected in your environment. Set one in `.env` (see `.env.example`).")

question = st.chat_input("Ask a question about the database...")

for turn in st.session_state.history:
    with st.chat_message("user"):
        st.write(turn["question"])
    with st.chat_message("assistant"):
        if turn.get("error"):
            st.error(turn["error"])
        else:
            st.write(turn["answer"])
            with st.expander("Show pipeline details"):
                st.markdown(f"**Retrieved tables:** {', '.join(turn['retrieved_tables'])}")
                for i, a in enumerate(turn["attempts"]):
                    tag = "✅" if a["valid"] else "❌"
                    st.code(a["sql"], language="sql")
                    if not a["valid"]:
                        st.caption(f"{tag} attempt {i+1} error: {a['error']}")
                if turn["columns"] and turn["rows"] is not None:
                    st.dataframe(pd.DataFrame(turn["rows"], columns=turn["columns"]))

if question:
    with st.chat_message("user"):
        st.write(question)
    with st.chat_message("assistant"):
        with st.spinner("Retrieving schema, generating SQL, validating, executing..."):
            try:
                result = run_pipeline(question, DB_PATH, retriever=st.session_state.retriever)
            except Exception as e:
                result = {"question": question, "error": f"Pipeline error: {e}",
                          "retrieved_tables": [], "attempts": []}

        if result.get("error"):
            st.error(result["error"])
        else:
            st.write(result["answer"])
            with st.expander("Show pipeline details"):
                st.markdown(f"**Retrieved tables:** {', '.join(result['retrieved_tables'])}")
                for i, a in enumerate(result["attempts"]):
                    tag = "✅" if a["valid"] else "❌"
                    st.code(a["sql"], language="sql")
                    if not a["valid"]:
                        st.caption(f"{tag} attempt {i+1} error: {a['error']}")
                if result["columns"] and result["rows"] is not None:
                    st.dataframe(pd.DataFrame(result["rows"], columns=result["columns"]))

    st.session_state.history.append(result)
