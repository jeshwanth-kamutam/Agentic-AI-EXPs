# Experiment 09 — Reasoning Model Benchmarking

## Objective
Build a benchmarking framework to empirically evaluate the performance (accuracy, latency, token usage) of different prompting strategies across a dataset.

## Problem Statement
Developers often guess which prompt strategy works best. Benchmarking replaces guesswork with data, allowing teams to balance cost (tokens/latency) against accuracy.

## Technologies Used
* Python
* Evaluation Framework Simulation

## Architecture
```text
Dataset (Q&A Pairs) -> LLM (Strategy A, B, C) -> Evaluation -> Metrics -> Comparison Report
```
Strategies compared:
1. Direct (Zero-shot)
2. Few-shot
3. Chain-of-Thought (Reasoning)

## Folder Structure
* `src/`: Core logic (`benchmark.py`)
* `tests/`: Pytest suite
* `run.py`: Entry point

## Installation
```bash
pip install -r requirements.txt
```

## Configuration
Copy `.env.example` to `.env`. This experiment uses a mock simulator by default (`MOCK_LLM=true`) to demonstrate the evaluation flow.

## How to Run
```bash
python run.py
```

## Sample Output
```text
Running benchmark on dataset (N=3)...

Strategy             | Accuracy   | Avg Latency  | Tokens
------------------------------------------------------------
Direct               | 33.3%      | 0.21s        | 64
Few-shot             | 66.7%      | 0.45s        | 135
Chain-of-Thought     | 100.0%     | 1.15s        | 345
```

## Explanation
The script iterates through a standard set of questions. For each question, it applies a different prompting strategy. It records whether the answer matches the expected baseline, how long it took, and how many tokens were consumed.

## Results
As prompting complexity increases (Direct -> Chain-of-Thought), accuracy generally increases, but so do latency and cost.

## Key Concepts Learned
- Prompt Benchmarking
- The Accuracy vs. Cost/Latency trade-off
- Standardized AI Evaluation

## Limitations
- The mock implementation uses hardcoded probabilities. Real evaluations require string matching or LLM-as-a-judge.

## Future Improvements
- Add an "LLM-as-a-Judge" evaluator to score complex generative outputs (like summaries) rather than exact-match Q&A.
