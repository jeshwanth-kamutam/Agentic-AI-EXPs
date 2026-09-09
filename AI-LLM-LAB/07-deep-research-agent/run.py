import os
from dotenv import load_dotenv
from src.researcher import DeepResearcher

def main():
    load_dotenv()
    print("--- 07: Deep Research Agent ---")
    
    researcher = DeepResearcher(use_mock=True)
    report = researcher.research("Quantum Computing")
    
    print("\n\n" + "="*40)
    print(report)
    print("="*40)

if __name__ == "__main__":
    main()
