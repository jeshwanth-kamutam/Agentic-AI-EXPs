import time
import random

class MockBenchmark:
    """Simulates benchmarking different prompting strategies."""
    
    def __init__(self):
        self.dataset = [
            {"q": "If I have 3 apples and give away 1, how many do I have?", "expected": "2"},
            {"q": "What is 15 * 3?", "expected": "45"},
            {"q": "Is the word 'racecar' a palindrome?", "expected": "yes"}
        ]

    def _simulate_llm_call(self, strategy: str, question: str) -> dict:
        """Simulates latency and accuracy based on the strategy."""
        latency = 0.0
        correct = False
        
        if strategy == "Direct":
            latency = random.uniform(0.1, 0.3)
            correct = random.choice([True, False]) # 50% chance
        elif strategy == "Few-shot":
            latency = random.uniform(0.3, 0.6)
            correct = random.choice([True, True, True, False]) # 75% chance
        elif strategy == "Chain-of-Thought":
            latency = random.uniform(0.8, 1.5)
            correct = True # 100% chance in this mock for math/logic
            
        return {"latency": latency, "correct": correct, "tokens": int(latency * 100)}

    def run_benchmark(self):
        strategies = ["Direct", "Few-shot", "Chain-of-Thought"]
        results = {}
        
        print("Running benchmark on dataset (N=3)...\n")
        
        for strategy in strategies:
            total_latency = 0
            correct_count = 0
            total_tokens = 0
            
            for item in self.dataset:
                res = self._simulate_llm_call(strategy, item["q"])
                total_latency += res["latency"]
                total_tokens += res["tokens"]
                if res["correct"]:
                    correct_count += 1
                    
            accuracy = (correct_count / len(self.dataset)) * 100
            avg_latency = total_latency / len(self.dataset)
            
            results[strategy] = {
                "Accuracy": f"{accuracy:.1f}%",
                "Avg Latency": f"{avg_latency:.2f}s",
                "Total Tokens": total_tokens
            }
            
        return results

    def print_report(self, results: dict):
        print(f"{'Strategy':<20} | {'Accuracy':<10} | {'Avg Latency':<12} | {'Tokens'}")
        print("-" * 60)
        for strategy, metrics in results.items():
            print(f"{strategy:<20} | {metrics['Accuracy']:<10} | {metrics['Avg Latency']:<12} | {metrics['Total Tokens']}")
