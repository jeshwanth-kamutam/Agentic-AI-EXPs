import os
from dotenv import load_dotenv
from src.db_setup import setup_database
from src.workflow import TextToSQLWorkflow

def main():
    load_dotenv()
    
    # Initialize the database
    setup_database("data/university.db")
    
    # Determine mode
    use_mock = os.getenv("MOCK_LLM", "true").lower() == "true"
    if use_mock:
        print("Running in MOCK mode (No API keys required).")
    else:
        print("Running with real LLM API.")
        
    workflow = TextToSQLWorkflow(db_path="data/university.db", use_mock=use_mock)
    
    questions = [
        "Show the top 5 students by marks.",
        "How many students are in each department?"
    ]
    
    for q in questions:
        result = workflow.run(q)
        print(f"\nFinal Answer: {result['final_answer']}\n")
        print("-" * 50)

if __name__ == "__main__":
    main()
