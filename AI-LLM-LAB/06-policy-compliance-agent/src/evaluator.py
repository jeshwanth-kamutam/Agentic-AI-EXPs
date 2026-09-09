class ComplianceEvaluator:
    """Evaluates text against a set of compliance rules."""
    
    def __init__(self, use_mock: bool = True):
        self.use_mock = use_mock
        self.policies = [
            "Rule 1: No sharing of Personally Identifiable Information (PII) like social security numbers or credit cards.",
            "Rule 2: No aggressive or threatening language.",
            "Rule 3: Financial advice must include a disclaimer."
        ]

    def _rule_based_check(self, text: str) -> str:
        """Simple regex/keyword based checks for obvious violations."""
        if "credit card" in text.lower() or "ssn" in text.lower():
            return "NON-COMPLIANT (Rule 1 violation detected by heuristic)"
        return "PASS_TO_AI"

    def _ai_evaluation(self, text: str) -> str:
        """Mock AI evaluation for complex Nuances."""
        text_lower = text.lower()
        if "i will destroy" in text_lower or "idiot" in text_lower:
            return "NON-COMPLIANT (Rule 2 violation detected by AI)"
        elif "buy this stock" in text_lower and "disclaimer" not in text_lower:
            return "NEEDS REVIEW (Rule 3 potential violation)"
        return "COMPLIANT"

    def evaluate(self, text: str) -> dict:
        print(f"Evaluating: '{text}'")
        
        # Step 1: Fast Rule-based verification
        heuristic_result = self._rule_based_check(text)
        if heuristic_result != "PASS_TO_AI":
            return {"status": "NON-COMPLIANT", "reason": heuristic_result, "text": text}
            
        # Step 2: Complex AI Evaluation
        ai_result = self._ai_evaluation(text)
        
        if "NON-COMPLIANT" in ai_result:
            return {"status": "NON-COMPLIANT", "reason": ai_result, "text": text}
        elif "NEEDS REVIEW" in ai_result:
            return {"status": "NEEDS REVIEW", "reason": ai_result, "text": text}
            
        return {"status": "COMPLIANT", "reason": "Passed all checks", "text": text}
