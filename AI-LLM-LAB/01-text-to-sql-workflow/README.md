# Experiment 01 — Text-to-SQL Workflow

## Objective
Build an end-to-end LLM workflow that translates natural language queries into SQL, executes them against a local SQLite database, and returns a natural language answer.

## Problem Statement
Users often want to query databases without knowing SQL. This experiment demonstrates how an LLM can map user intents to a database schema, generate valid SQL, and synthesize the database output.

## Technologies Used
* Python
* SQLite3
* LangChain (Optional for LLM orchestration)
* Pytest (Testing)

## Architecture
```text
Question -> Schema Retrieval -> Prompt -> SQL Generation -> SQL Validation -> DB Execution -> NL Answer
```

## Folder Structure
* `src/`: Core logic (`workflow.py`, `db_setup.py`)
* `data/`: SQLite database files
* `tests/`: Pytest test suite
* `run.py`: Entry point

## Installation
```bash
pip install -r requirements.txt
```

## Configuration
Copy `.env.example` to `.env`. By default, this lab uses a Mock LLM (`MOCK_LLM=true`) to demonstrate the flow without requiring API keys.

## How to Run
```bash
python run.py
```

## Sample Input
```text
"Show the top 5 students by marks."
```

## Sample Output
```text
1. Retrieving Schema...
2. Generating SQL...
   Generated SQL: SELECT name, marks FROM students ORDER BY marks DESC LIMIT 5;
3. Executing SQL...
   Query Results: [('Alice Smith', 95), ('Diana Prince', 92), ('Fiona Gallagher', 90), ('Bob Johnson', 88), ('Evan Wright', 85)]
4. Generating Natural Language Answer...

Final Answer: The top students by marks are Alice Smith (95), Diana Prince (92), Fiona Gallagher (90), Bob Johnson (88), and Evan Wright (85).
```

## Explanation
The script first pulls the DDL from `sqlite_master`. It sends this schema along with the question to the LLM to write the query. After execution, it sends the raw tuple results back to the LLM to frame into a human-readable response.

## Results
The mock workflow successfully emulates a real text-to-sql pipeline locally.

## Key Concepts Learned
- Prompt Engineering for structured output (SQL)
- Retrieval of contextual metadata (Database Schema)
- Chaining LLM calls (Generation -> Execution -> Synthesis)

## Limitations
- Complex joins or nested queries often require few-shot prompting to work reliably.
- Prone to SQL injection if not properly sanitized in production.

## Future Improvements
- Add a semantic layer (descriptions of tables/columns).
- Implement retry logic if the generated SQL fails validation.
