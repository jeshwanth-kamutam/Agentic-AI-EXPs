from src.benchmark import MockBenchmark

def test_benchmark_run():
    benchmark = MockBenchmark()
    results = benchmark.run_benchmark()
    assert "Direct" in results
    assert "Few-shot" in results
    assert "Chain-of-Thought" in results
    assert "Accuracy" in results["Chain-of-Thought"]
