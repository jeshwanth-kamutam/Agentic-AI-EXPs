from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

def get_vectorstore(persist_directory="./chroma_db"):
    """Loads the existing ChromaDB vector store."""
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = Chroma(
        persist_directory=persist_directory,
        embedding_function=embeddings
    )
    return vectorstore

def get_retriever(vectorstore, search_kwargs={"k": 3}):
    """Returns a retriever object from the vector store."""
    return vectorstore.as_retriever(search_kwargs=search_kwargs)
