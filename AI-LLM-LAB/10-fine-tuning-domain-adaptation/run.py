import os
from dotenv import load_dotenv
from src.finetuner import MockFineTuner

def main():
    load_dotenv()
    print("--- 10: Fine-Tuning for Domain Adaptation ---")
    print("Note: This script runs in a mock simulation mode for educational purposes.")
    print("Real fine-tuning requires a GPU and libraries like 'transformers', 'peft', and 'trl'.\n")
    
    finetuner = MockFineTuner()
    finetuner.run_pipeline()

if __name__ == "__main__":
    main()
