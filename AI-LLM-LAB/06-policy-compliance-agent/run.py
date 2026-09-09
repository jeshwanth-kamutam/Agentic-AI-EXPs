import os
from dotenv import load_dotenv
from src.evaluator import ComplianceEvaluator

def main():
    load_dotenv()
    use_mock = os.getenv("MOCK_LLM", "true").lower() == "true"
    
    print("--- 06: Policy Compliance Agent ---")
    
    evaluator = ComplianceEvaluator(use_mock=use_mock)
    
    test_cases = [
        "Hello, I would like to update my address.",
        "Here is my credit card number to pay for the order.",
        "You are an idiot and I will destroy your company.",
        "You should definitely buy this stock right now, it will go to the moon!"
    ]
    
    for case in test_cases:
        result = evaluator.evaluate(case)
        print(f"Status: {result['status']}")
        print(f"Reason: {result['reason']}\n")

if __name__ == "__main__":
    main()
