import streamlit as st
import os
from src.indexing import load_documents, chunk_documents, index_documents
from src.rag_chain import setup_rag_chain, ask_question
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="RAG Agent QA", page_icon="🤖", layout="wide")

st.title("🤖 RAG-Based Document QA System")
st.markdown("Upload a PDF or Text file and ask questions about its content! Built with LangChain, ChromaDB, and Groq.")

# Initialize session state for RAG chain
if "rag_chain" not in st.session_state:
    st.session_state.rag_chain = None

# Sidebar for configuration and uploading
with st.sidebar:
    st.header("1. Settings")
    groq_api_key = st.text_input("Groq API Key", type="password", value=os.environ.get("GROQ_API_KEY", ""))
    
    if groq_api_key:
        os.environ["GROQ_API_KEY"] = groq_api_key

    st.header("2. Upload Document")
    uploaded_file = st.file_uploader("Upload a file", type=["pdf", "txt"])
    
    if st.button("Index Document") and uploaded_file and groq_api_key:
        with st.spinner("Processing document..."):
            # Save uploaded file temporarily
            temp_path = f"./{uploaded_file.name}"
            with open(temp_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            try:
                # 1. Load
                st.info("Loading document...")
                docs = load_documents(temp_path)
                
                # 2. Chunk
                st.info("Chunking document...")
                chunks = chunk_documents(docs)
                
                # 3. Index
                st.info("Creating vector embeddings...")
                index_documents(chunks)
                
                # Setup retrieval chain
                st.session_state.rag_chain = setup_rag_chain()
                st.success("Document indexed successfully! You can now ask questions.")
            except Exception as e:
                st.error(f"Error processing document: {e}")
            finally:
                if os.path.exists(temp_path):
                    os.remove(temp_path)

# Chat Interface
if st.session_state.rag_chain:
    st.header("3. Ask a Question")
    question = st.text_input("Enter your question:")
    
    if st.button("Generate Answer") and question:
        with st.spinner("Thinking..."):
            try:
                answer = ask_question(st.session_state.rag_chain, question)
                st.write("**Answer:**")
                st.write(answer)
            except Exception as e:
                st.error(f"Error generating answer: {e}")
else:
    st.info("Please enter your Groq API key and upload/index a document in the sidebar to start asking questions.")
