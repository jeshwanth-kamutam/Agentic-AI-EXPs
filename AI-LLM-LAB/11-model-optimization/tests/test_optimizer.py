from src.optimizer import MockQuantizer

def test_optimization():
    opt = MockQuantizer()
    res = opt.optimize("fp32", "int8")
    assert res["size_gb"] < 14.0
    assert res["latency_ms"] < 120
