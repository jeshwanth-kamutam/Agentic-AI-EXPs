import os

def load_sample_documents():
    """Returns sample documents for the RAG system."""
    return [
        {"id": "doc1", "text": "Artificial Intelligence is the simulation of human intelligence processes by machines, especially computer systems."},
        {"id": "doc2", "text": "Retrieval-Augmented Generation (RAG) is an AI framework for retrieving facts from an external knowledge base to ground large language models on the most accurate, up-to-date information."},
        {"id": "doc3", "text": "Large Language Models (LLMs) are deep learning models trained on massive amounts of data to understand and generate natural language."},
        {"id": "doc4", "text": "A vector database is a type of database that stores and manages unstructured data, such as text, images, or audio, in the form of high-dimensional vectors."}
    ]

def chunk_text(text: str, chunk_size: int = 50) -> list:
    """A naive chunking function."""
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunks.append(" ".join(words[i:i+chunk_size]))
    return chunks

def process_documents(documents: list):
    """Chunks documents into smaller pieces."""
    processed = []
    for doc in documents:
        chunks = chunk_text(doc["text"])
        for idx, chunk in enumerate(chunks):
            processed.append({"id": f"{doc['id']}_{idx}", "text": chunk})
    return processed
