import os
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

def load_documents(file_path):
    """Loads a PDF or TXT file."""
    if file_path.endswith('.pdf'):
        loader = PyPDFLoader(file_path)
    elif file_path.endswith('.txt'):
        loader = TextLoader(file_path)
    else:
        raise ValueError("Unsupported file format. Please upload a PDF or TXT file.")
    return loader.load()

def chunk_documents(documents, chunk_size=1000, chunk_overlap=200):
    """Splits documents into smaller chunks."""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return text_splitter.split_documents(documents)

def index_documents(documents, persist_directory="./chroma_db"):
    """Indexes document chunks into a ChromaDB vector store."""
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory=persist_directory
    )
    return vectorstore
