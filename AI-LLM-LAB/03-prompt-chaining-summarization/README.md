# Experiment 03 — Prompt Chaining for Summarization

## Objective
Build a multi-step summarization pipeline using prompt chaining to improve output quality over single-shot prompting.

## Problem Statement
Asking an LLM to perform complex tasks (like summarizing a long, dense document while maintaining high professional quality and structure) in a single prompt often leads to suboptimal results. By breaking the task into smaller steps (chaining), the LLM can focus on one sub-task at a time.

## Technologies Used
* Python
* Prompt Engineering Concepts

## Architecture
```text
Input Document -> Extract Facts -> Generate Structured Summary -> Refine Summary -> Final Output
```

## Folder Structure
* `src/`: Core logic (`pipeline.py`)
* `tests/`: Pytest suite
* `run.py`: Entry point

## Installation
```bash
pip install -r requirements.txt
```

## Configuration
Copy `.env.example` to `.env`. This experiment supports a Mock LLM (`MOCK_LLM=true`).

## How to Run
```bash
python run.py
```

## Sample Input
A dense paragraph about AI, ethics, and RAG.

## Sample Output
```text
=== APPROACH 1: Single Prompt Summarization ===
AI transforms industries but raises ethical/bias concerns. RAG is used to improve factual accuracy and reduce hallucinations.

=== APPROACH 2: Multi-Step Prompt Chaining ===
Step 1: Extracting facts...
Step 2: Generating initial draft...
Step 3: Refining summary...

[Final] Refined Summary:
### The State of AI: Transformations and Challenges
Artificial Intelligence is driving transformative changes across multiple industries. Despite this rapid progress, developers face critical challenges regarding ethical deployment and algorithmic bias. To mitigate issues like hallucination and ensure factual grounding, the industry is increasingly adopting Retrieval-Augmented Generation (RAG) frameworks.
```

## Explanation
The code compares a single `summarize this` prompt against a 3-step chain:
1. Extract Bullet Points
2. Generate Draft from Bullets
3. Refine Draft for vocabulary and flow

## Results
The chained output is significantly more structured, comprehensive, and professionally written than the single-prompt output.

## Key Concepts Learned
- Prompt Chaining
- Task Decomposition for LLMs
- Self-Correction / Iterative refinement

## Limitations
- Increases token usage (cost) and latency because multiple API calls are required instead of one.

## Future Improvements
- Add a conditional routing step (e.g., only route to the refinement step if a quality check LLM call deems the draft inadequate).
