# Experiment 07 — Deep Research Agent Workflow

## Objective
Build an agentic workflow that breaks down a complex research topic into sub-queries, gathers information, drafts a report, critiques its own draft, and synthesizes a final document.

## Problem Statement
Standard LLM generation often results in shallow or poorly structured answers for complex topics. A deep research workflow mimics human research by planning, gathering, drafting, and reflecting.

## Technologies Used
* Python
* Self-Reflection Loop Simulation

## Architecture
```text
Topic -> Plan (Sub-queries) -> Gather (Search) -> Draft -> Reflect (Critique) -> Final Report
```

## Folder Structure
* `src/`: Core logic (`researcher.py`)
* `tests/`: Pytest suite
* `run.py`: Entry point

## Installation
```bash
pip install -r requirements.txt
```

## Configuration
Copy `.env.example` to `.env`. This experiment uses mock search and LLM data by default to run without paid API keys (`MOCK_LLM=true`).

## How to Run
```bash
python run.py
```

## Sample Input
```text
Topic: "Quantum Computing"
```

## Sample Output
```text
=== Starting Deep Research on: 'Quantum Computing' ===

[Planning] Breaking down the research topic into sub-queries...

[Gathering] Simulating web searches for queries...
  -> Searching: History of Quantum Computing
  -> Searching: Current state of Quantum Computing
  -> Searching: Future implications of Quantum Computing

[Drafting] Synthesizing evidence into an initial report...

[Reflection] Reviewing draft for gaps and logic errors...
  -> Critique: The draft is a bit repetitive and lacks a strong conclusion.

[Finalizing] Generating final report based on reflection...

========================================
## Comprehensive Research Report
### History of Quantum Computing
Mock evidence found for 'History of Quantum Computing': The topic has evolved significantly.
...
### Conclusion
Based on the analysis, this field will continue to grow rapidly.
========================================
```

## Explanation
The `DeepResearcher` class implements the standard Plan-and-Solve paradigm combined with Self-Reflection. It explicitly pauses at the reflection step to generate a critique of its own draft, which is then used to refine the final output.

## Results
The structured approach forces the system to consider multiple angles (history, current state, future) and explicitly add a conclusion via reflection.

## Key Concepts Learned
- Agentic Planning
- Self-Reflection / Self-Critique
- Iterative Refinement

## Limitations
- Mock web search doesn't retrieve real data.
- True reflection requires a very capable LLM to avoid "rubber stamping" bad drafts.

## Future Improvements
- Integrate actual web search tools (e.g., DuckDuckGo API, SerpAPI).
- Add recursive research loops where critique triggers further data gathering.
