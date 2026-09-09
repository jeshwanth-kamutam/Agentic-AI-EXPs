# Experiment 06 — Policy Compliance Agent

## Objective
Build an AI agent that evaluates input text against a strict set of corporate compliance policies, using a hybrid approach of rule-based heuristics and AI evaluation.

## Problem Statement
Relying solely on LLMs for compliance is expensive, slow, and sometimes non-deterministic. Relying solely on regex/rules misses nuanced violations. A hybrid approach combines the speed of heuristics with the reasoning of an LLM.

## Technologies Used
* Python
* Rule-based parsing
* LLM Evaluation logic

## Architecture
```text
Input Content -> Policy Rules -> Rule-Based Verification (Fast Fail) -> AI Evaluation (Nuance) -> Compliance Decision -> Explanation
```

## Folder Structure
* `src/`: Core logic (`evaluator.py`)
* `tests/`: Pytest suite
* `run.py`: Entry point

## Installation
```bash
pip install -r requirements.txt
```

## Configuration
Copy `.env.example` to `.env`. This experiment uses a Mock LLM by default (`MOCK_LLM=true`) to demonstrate the logic. *Note: Data used here is purely synthetic for educational purposes.*

## How to Run
```bash
python run.py
```

## Sample Input
```text
"Here is my credit card number to pay for the order."
"You are an idiot and I will destroy your company."
```

## Sample Output
```text
Evaluating: 'Here is my credit card number to pay for the order.'
Status: NON-COMPLIANT
Reason: NON-COMPLIANT (Rule 1 violation detected by heuristic)

Evaluating: 'You are an idiot and I will destroy your company.'
Status: NON-COMPLIANT
Reason: NON-COMPLIANT (Rule 2 violation detected by AI)
```

## Explanation
The `ComplianceEvaluator` first runs a fast, cheap rule-based check (e.g. looking for obvious restricted strings like "credit card"). If it passes, it is forwarded to the AI evaluator, which checks for nuanced policy violations (like aggressive language or missing financial disclaimers).

## Results
The agent correctly classifies inputs into COMPLIANT, NON-COMPLIANT, or NEEDS REVIEW based on the defined policies.

## Key Concepts Learned
- Hybrid AI architectures (Heuristics + LLMs)
- Content Moderation / Guardrails
- Cost-saving routing in AI applications

## Limitations
- The mock AI relies on simple string matching rather than true semantic understanding.
- Real compliance requires highly specialized fine-tuned models rather than general LLMs.

## Future Improvements
- Implement a true LLM call with a strict system prompt (e.g. outputting JSON with `status` and `reason`).
- Add integration with a real PII detection library (like Microsoft Presidio).
