def generate_answer(query: str, retrieved_docs: list, use_mock: bool = True) -> str:
    """Generates an answer using the retrieved context."""
    
    context = "\n".join([f"- {doc['text']}" for doc in retrieved_docs])
    
    prompt = f"""
    Use the following pieces of context to answer the question at the end.
    If you don't know the answer based on the context, just say that you don't know, don't try to make up an answer.

    Context:
    {context}

    Question: {query}
    Answer:
    """
    
    if use_mock:
        # Mock LLM generation logic
        query_lower = query.lower()
        if "rag" in query_lower:
            return "RAG stands for Retrieval-Augmented Generation. It is an AI framework that retrieves facts from an external knowledge base to ground language models."
        elif "llm" in query_lower or "language models" in query_lower:
            return "Large Language Models (LLMs) are deep learning models trained on massive amounts of data to understand and generate natural language."
        elif "vector" in query_lower:
            return "A vector database stores and manages unstructured data in the form of high-dimensional vectors."
        else:
            return "Based on the provided context, I don't have enough information to answer that question."
    
    # Real LLM Call would go here
    raise NotImplementedError("Real LLM call not implemented. Set MOCK_LLM=true.")
