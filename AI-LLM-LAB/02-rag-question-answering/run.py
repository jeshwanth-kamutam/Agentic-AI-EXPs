import os
from dotenv import load_dotenv
from src.document_processor import load_sample_documents, process_documents
from src.retriever import MockRetriever
from src.generator import generate_answer

def main():
    load_dotenv()
    use_mock = os.getenv("MOCK_LLM", "true").lower() == "true"
    
    print("--- 02: RAG Question Answering System ---")
    
    print("\n1. Loading and Chunking Documents...")
    raw_docs = load_sample_documents()
    processed_docs = process_documents(raw_docs)
    
    print("\n2. Generating Embeddings and Initializing Vector Store...")
    retriever = MockRetriever(processed_docs)
    
    questions = [
        "What is RAG?",
        "What are Large Language Models?",
        "How do you bake a cake?"
    ]
    
    for q in questions:
        print(f"\n--- Question: '{q}' ---")
        
        print("3. Retrieving Relevant Context...")
        relevant_docs = retriever.retrieve(q)
        for d in relevant_docs:
            print(f"   -> Retrieved: {d['text'][:60]}...")
            
        print("4. Generating Answer...")
        answer = generate_answer(q, relevant_docs, use_mock=use_mock)
        print(f"   -> Answer: {answer}")

if __name__ == "__main__":
    main()
