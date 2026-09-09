from src.researcher import DeepResearcher

def test_research_plan():
    researcher = DeepResearcher(use_mock=True)
    plan = researcher.plan("AI")
    assert len(plan) == 3

def test_full_research():
    researcher = DeepResearcher(use_mock=True)
    res = researcher.research("AI")
    assert "Conclusion" in res
    assert "Comprehensive Research Report" in res
