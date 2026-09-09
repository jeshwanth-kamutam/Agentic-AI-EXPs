from src.agents import LeadGenerationAgent, LeadQualificationAgent

def test_lead_generation():
    agent = LeadGenerationAgent()
    res = agent.process({})
    assert "leads" in res
    assert len(res["leads"]) == 2

def test_lead_qualification():
    agent = LeadQualificationAgent()
    context = {"leads": [{"name": "Test", "title": "CTO"}]}
    res = agent.process(context)
    assert len(res["qualified_leads"]) == 1
    assert res["qualified_leads"][0]["score"] == 90
