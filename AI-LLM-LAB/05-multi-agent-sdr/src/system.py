from src.agents import LeadGenerationAgent, LeadQualificationAgent, EmailGenerationAgent, ReviewAgent
import time

class SDRSystem:
    def __init__(self):
        self.agents = [
            LeadGenerationAgent(),
            LeadQualificationAgent(),
            EmailGenerationAgent(),
            ReviewAgent()
        ]

    def run(self):
        print("Starting Multi-Agent SDR Workflow...")
        context = {}
        for agent in self.agents:
            context = agent.process(context)
            time.sleep(0.5)
        
        print("\n=== Workflow Complete ===")
        print(f"Final Approved Emails: {len(context.get('final_emails', []))}")
        for email in context.get("final_emails", []):
            print(f"\nTo: {email['lead']['name']} ({email['lead']['company']})")
            print(f"Body: {email['final_email']}")
