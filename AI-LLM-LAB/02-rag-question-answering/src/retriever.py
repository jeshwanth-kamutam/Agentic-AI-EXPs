import numpy as np

class MockRetriever:
    """A mock vector retriever for educational purposes."""
    
    def __init__(self, documents):
        self.documents = documents
        # In a real app, you would compute sentence embeddings here and store them in FAISS or Chroma.
        # embeddings = embedder.encode([doc['text'] for doc in self.documents])
        # index = faiss.IndexFlatL2(embedding_dim)
        # index.add(embeddings)
        print("Vector Database Initialized with", len(self.documents), "chunks.")
        
    def retrieve(self, query: str, top_k: int = 2):
        """Mock similarity search."""
        query_lower = query.lower()
        results = []
        
        # Simple keyword matching as a mock for semantic search
        for doc in self.documents:
            score = 0
            for word in query_lower.split():
                if word in doc['text'].lower():
                    score += 1
            if score > 0:
                results.append((score, doc))
        
        # Sort by score and take top_k
        results.sort(key=lambda x: x[0], reverse=True)
        return [doc for score, doc in results[:top_k]]
