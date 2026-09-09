# Experiment 02 — RAG-Based Question Answering System

## Objective
Build a complete Retrieval-Augmented Generation (RAG) system to answer questions using an external knowledge base.

## Problem Statement
Large Language Models have knowledge cutoffs and can hallucinate. RAG solves this by retrieving relevant documents from a knowledge base and providing them as context to the LLM.

## Technologies Used
* Python
* Vector Search Simulation
* Document Processing logic

## Architecture
```text
Documents -> Chunking -> Embeddings -> Vector Database -> Retriever -> Relevant Context -> LLM -> Answer
```

## Folder Structure
* `src/`: Core logic (`document_processor.py`, `retriever.py`, `generator.py`)
* `data/`: Sample documents (internal to code in this basic version)
* `tests/`: Pytest suite
* `run.py`: Entry point

## Installation
```bash
pip install -r requirements.txt
```

## Configuration
Copy `.env.example` to `.env`. This experiment supports a Mock LLM (`MOCK_LLM=true`) to demonstrate the RAG flow without paid API keys.

## How to Run
```bash
python run.py
```

## Sample Input
```text
"What is RAG?"
```

## Sample Output
```text
1. Loading and Chunking Documents...

2. Generating Embeddings and Initializing Vector Store...
Vector Database Initialized with 4 chunks.

--- Question: 'What is RAG?' ---
3. Retrieving Relevant Context...
   -> Retrieved: Retrieval-Augmented Generation (RAG) is an AI framework for ...
4. Generating Answer...
   -> Answer: RAG stands for Retrieval-Augmented Generation. It is an AI framework that retrieves facts from an external knowledge base to ground language models.
```

## Explanation
The system reads a set of raw text documents, splits them into manageable chunks, and indexes them in a mock vector database. When a query is asked, it searches for chunks containing similar keywords, injects those chunks into a prompt, and generates the final answer.

## Results
The system successfully grounds its answers in the provided documents, avoiding hallucinations. For out-of-domain questions (e.g. "How to bake a cake"), it correctly identifies that it lacks the context to answer.

## Key Concepts Learned
- Text Chunking
- Vector Search / Information Retrieval
- Context Window Management
- Hallucination mitigation

## Limitations
- This mock version uses keyword search instead of true semantic embedding search (like FAISS/Chroma).
- Naive chunking can split sentences midway.

## Future Improvements
- Integrate `sentence-transformers` for true semantic dense embeddings.
- Add document loaders (PDF, HTML).
