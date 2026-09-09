from src.db_setup import setup_database
from src.agent import ReActSQLAgent
import os
from dotenv import load_dotenv

def main():
    load_dotenv()
    print("--- 04: SQL Agent with Tool Use ---")
    setup_database()
    
    agent = ReActSQLAgent()
    questions = [
        "What is the most expensive product?"
    ]
    
    for q in questions:
        agent.run(q)

if __name__ == "__main__":
    main()
