# Experiment 12 — Mini Project / Capstone: Agentic AI System

## Objective
Build an end-to-end agentic AI system combining RAG (for unstructured text), SQL Tools (for structured databases), and Multi-Agent Routing into a single cohesive application.

## Problem Statement
Real-world enterprise applications don't rely on a single AI technique. Answering a complex business question often requires pulling numbers from a database, checking rules from a PDF policy document, and combining them. This capstone unifies the concepts from previous experiments.

## Technologies Used
* Python
* SQLite3
* Multi-Agent Orchestration (Master/Router Agent + Specialist Agents)

## Architecture
```text
                  USER
                    │
                    ▼
              MASTER AGENT (Router)
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
      RAG AGENT           SQL AGENT
    (Unstructured)       (Structured)
          │                   │
          ▼                   ▼
     Vector DB             Database
          │                   │
          └─────────┬─────────┘
                    ▼
               FINAL ANSWER
```

## Folder Structure
* `src/`: Core logic (`capstone.py`, `db_setup.py`)
* `data/`: SQLite databases
* `tests/`: Pytest suite
* `run.py`: Entry point

## Installation
```bash
pip install -r requirements.txt
```

## Configuration
Copy `.env.example` to `.env`. This experiment uses a mock simulation to demonstrate the architecture without requiring complex multi-LLM API setups.

## How to Run
```bash
python run.py
```

## Sample Input
```text
"What is Alice's expected bonus?"
```

## Sample Output
```text
=== Master Agent Received Query: 'What is Alice's expected bonus?' ===
[Master Agent] Decomposing query...
[Master Agent] Routing to SQL Agent for employee details...
[SQL Agent] Querying DB for Alice's salary...
[Master Agent] Routing to RAG Agent for bonus policy...
[RAG Agent] Searching vector DB for policy...
[Master Agent] Synthesizing final answer...

Final Output:
Alice is in Engineering with a salary of $120000.0. According to policy, her bonus is $12000.0.
```

## Explanation
The `MasterAgent` receives a complex query and determines it needs two pieces of information: the employee's salary (structured data) and the bonus calculation rules (unstructured text). It delegates these sub-tasks to the `SQLAgent` and `RAGAgent` respectively, gathers the results, performs the math, and returns the final answer.

## Results
The system successfully bridges structured and unstructured data silos using AI agents.

## Key Concepts Learned
- Agent Orchestration and Routing
- Unifying RAG and Tool Use
- Complex Query Decomposition

## Limitations
- Hardcoded routing logic in this mock. Real systems use an LLM router (e.g., semantic routing).

## Future Improvements
- Implement a true LLM-based router (using tools like LangGraph or Semantic Router) to dynamically choose which agent to call based on the user's prompt.
