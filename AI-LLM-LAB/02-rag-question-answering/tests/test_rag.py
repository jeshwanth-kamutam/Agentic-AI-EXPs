import pytest
from src.document_processor import load_sample_documents, chunk_text
from src.retriever import MockRetriever

def test_document_processor():
    docs = load_sample_documents()
    assert len(docs) > 0
    chunks = chunk_text("This is a test document with several words to be chunked into pieces.", chunk_size=5)
    assert len(chunks) == 3

def test_retriever():
    docs = [{"id": "1", "text": "Apple is a fruit."}, {"id": "2", "text": "Car is a vehicle."}]
    retriever = MockRetriever(docs)
    results = retriever.retrieve("What is an apple?")
    assert len(results) > 0
    assert "Apple" in results[0]["text"]
