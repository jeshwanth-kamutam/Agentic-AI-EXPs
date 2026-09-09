# Experiment 05 — Multi-Agent SDR System

## Objective
Build a simulated Sales Development Representative (SDR) workflow utilizing a multi-agent architecture where agents pass context sequentially to accomplish a complex goal.

## Problem Statement
Complex tasks (like finding a lead, evaluating them, drafting a personalized email, and reviewing it) are too difficult for a single LLM call to handle reliably. A multi-agent system divides the labor among specialized roles.

## Technologies Used
* Python
* Sequential Multi-Agent orchestration (Conceptual)

## Architecture
```text
Lead Generation Agent -> Lead Qualification Agent -> Email Generation Agent -> Review Agent
```

## Folder Structure
* `src/`: Core logic (`agents.py`, `system.py`)
* `tests/`: Pytest suite
* `run.py`: Entry point

## Installation
```bash
pip install -r requirements.txt
```

## Configuration
Copy `.env.example` to `.env`. Uses a mock system by default. Note: No real emails are sent in this experiment.

## How to Run
```bash
python run.py
```

## Sample Output
```text
Starting Multi-Agent SDR Workflow...
[Lead Generation Agent] Finding leads in target industry...
[Lead Qualification Agent] Scoring leads...
[Email Generation Agent] Drafting emails for qualified leads...
[Review Agent] Reviewing drafts for compliance and tone...

=== Workflow Complete ===
Final Approved Emails: 1

To: John Doe (TechCorp)
Body: Hi John Doe, I noticed TechCorp is growing. We can help scale your engineering team.

Best, SDR Team
```

## Explanation
Each agent is represented as a distinct Python class. The system orchestrator passes a shared `context` dictionary between them. Each agent reads from the context, performs its specialized task, and writes the results back to the context for the next agent.

## Results
The sequential agent chain successfully filters out unqualified leads and only drafts and approves emails for highly qualified targets.

## Key Concepts Learned
- Multi-Agent Systems
- State / Context passing between agents
- Role specialization

## Limitations
- This is a sequential chain; it does not support complex routing (e.g., if the Review Agent rejects the draft, it cannot currently send it back to the Generation Agent).

## Future Improvements
- Integrate a framework like LangGraph or AutoGen for cyclic graphs and state management.
