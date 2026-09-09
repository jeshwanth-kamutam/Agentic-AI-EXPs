import os
from dotenv import load_dotenv
from src.db_setup import setup_database
from src.capstone import MasterAgent

def main():
    load_dotenv()
    print("--- 12: Capstone Agentic System ---")
    setup_database()
    
    agent = MasterAgent()
    
    query = "What is Alice's expected bonus?"
    result = agent.process(query)
    
    print(f"\nFinal Output:\n{result}")

if __name__ == "__main__":
    main()
