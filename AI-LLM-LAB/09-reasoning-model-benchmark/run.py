import os
from dotenv import load_dotenv
from src.benchmark import MockBenchmark

def main():
    load_dotenv()
    print("--- 09: Reasoning Model Benchmarking ---")
    
    benchmark = MockBenchmark()
    results = benchmark.run_benchmark()
    benchmark.print_report(results)

if __name__ == "__main__":
    main()
