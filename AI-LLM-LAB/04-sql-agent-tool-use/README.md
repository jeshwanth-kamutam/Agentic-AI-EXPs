# Experiment 04 — SQL Agent with Tool Use

## Objective
Build a ReAct-style agent that can autonomously navigate a database using specific tools (listing tables, getting schemas, and executing SQL).

## Problem Statement
Standard Text-to-SQL (Experiment 01) fails if the schema is too large to fit in the prompt, or if the LLM needs to explore the database interactively to understand the data before answering. An Agent with tools solves this by acting autonomously in a loop.

## Technologies Used
* Python
* SQLite3
* Agent Framework simulation

## Architecture
```text
Agent -> Thought -> Action (Tool) -> Observation -> (Loop) -> Final Answer
```
Tools provided:
1. `list_tables()`
2. `get_schema(table_name)`
3. `execute_sql(sql)`

## Folder Structure
* `src/`: Core logic (`agent.py`, `tools.py`, `db_setup.py`)
* `data/`: SQLite databases
* `tests/`: Pytest suite
* `run.py`: Entry point

## Installation
```bash
pip install -r requirements.txt
```

## Configuration
Copy `.env.example` to `.env`. Uses mock mode by default.

## How to Run
```bash
python run.py
```

## Sample Input
```text
"What is the most expensive product?"
```

## Sample Output
```text
[Agent Started] Goal: What is the most expensive product?
[Agent Action] Calling tool: list_tables()
[Tool Result] Tables: products
[Agent Action] Calling tool: get_schema(table_name='products')
[Tool Result] CREATE TABLE products (...)
[Agent Action] Calling tool: execute_sql(sql='SELECT name, price FROM products ORDER BY price DESC LIMIT 1;')
[Tool Result] Results: [('Laptop', 999.99)]
[Agent Action] Formulating final answer...

[Final Answer] The most expensive product is the Laptop at $999.99.
```

## Explanation
The agent is given a goal and a set of tools. Instead of predicting the final answer immediately, it predicts the *next action* to take. It observes the result, then predicts the next action, until it has enough information to synthesize the final answer.

## Results
The agent successfully uses iterative exploration to find the answer.

## Key Concepts Learned
- ReAct (Reasoning and Acting) paradigm
- LLM Tool Calling / Function Calling
- Autonomous exploration of environments

## Limitations
- Agents can easily get stuck in infinite loops if a tool repeatedly returns an error.
- High latency and cost due to multiple LLM calls per query.

## Future Improvements
- Add a tool to get sample rows (e.g. `SELECT * FROM table LIMIT 3`) to help the LLM understand data formatting.
- Implement a maximum iteration limit to prevent infinite loops.
