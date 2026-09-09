class MockAgent:
    """Base class for mock agents."""
    def __init__(self, name: str):
        self.name = name
    
    def process(self, context: dict) -> dict:
        pass

class LeadGenerationAgent(MockAgent):
    def __init__(self):
        super().__init__("Lead Generation Agent")

    def process(self, context: dict) -> dict:
        print(f"[{self.name}] Finding leads in target industry...")
        context["leads"] = [
            {"name": "John Doe", "title": "CTO", "company": "TechCorp", "industry": "Software"},
            {"name": "Jane Smith", "title": "Marketing Manager", "company": "RetailInc", "industry": "Retail"}
        ]
        return context

class LeadQualificationAgent(MockAgent):
    def __init__(self):
        super().__init__("Lead Qualification Agent")

    def process(self, context: dict) -> dict:
        print(f"[{self.name}] Scoring leads...")
        qualified = []
        for lead in context.get("leads", []):
            if lead["title"] == "CTO":
                lead["score"] = 90
                lead["status"] = "QUALIFIED"
                qualified.append(lead)
            else:
                lead["score"] = 40
                lead["status"] = "DISQUALIFIED"
        context["qualified_leads"] = qualified
        return context

class EmailGenerationAgent(MockAgent):
    def __init__(self):
        super().__init__("Email Generation Agent")

    def process(self, context: dict) -> dict:
        print(f"[{self.name}] Drafting emails for qualified leads...")
        drafts = []
        for lead in context.get("qualified_leads", []):
            draft = f"Hi {lead['name']}, I noticed TechCorp is growing. We can help scale your engineering team."
            drafts.append({"lead": lead, "draft": draft})
        context["drafts"] = drafts
        return context

class ReviewAgent(MockAgent):
    def __init__(self):
        super().__init__("Review Agent")

    def process(self, context: dict) -> dict:
        print(f"[{self.name}] Reviewing drafts for compliance and tone...")
        final_emails = []
        for item in context.get("drafts", []):
            draft = item["draft"]
            # Mock review process
            final_email = draft + "\n\nBest, SDR Team"
            final_emails.append({"lead": item["lead"], "final_email": final_email, "approved": True})
        context["final_emails"] = final_emails
        return context
