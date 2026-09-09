from src.evaluator import ComplianceEvaluator

def test_compliant():
    evaluator = ComplianceEvaluator(use_mock=True)
    res = evaluator.evaluate("Hello world")
    assert res["status"] == "COMPLIANT"

def test_rule_violation():
    evaluator = ComplianceEvaluator(use_mock=True)
    res = evaluator.evaluate("My credit card is 1234")
    assert res["status"] == "NON-COMPLIANT"

def test_ai_violation():
    evaluator = ComplianceEvaluator(use_mock=True)
    res = evaluator.evaluate("You are an idiot")
    assert res["status"] == "NON-COMPLIANT"
