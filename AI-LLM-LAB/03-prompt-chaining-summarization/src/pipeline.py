class MockLLM:
    """Mock LLM to simulate the chaining process."""
    def generate(self, prompt: str) -> str:
        prompt_lower = prompt.lower()
        if "extract the most important key facts" in prompt_lower:
            return "- AI is transforming industries.\n- Ethics and bias are major concerns.\n- RAG improves factual accuracy."
        elif "generate a structured summary" in prompt_lower:
            return "## AI Overview\n\nAI is currently transforming many industries. However, there are significant concerns regarding ethics and bias in AI models. To address hallucination and factual accuracy, techniques like RAG (Retrieval-Augmented Generation) are increasingly used."
        elif "improve and refine the following summary" in prompt_lower:
            return "### The State of AI: Transformations and Challenges\n\nArtificial Intelligence is driving transformative changes across multiple industries. Despite this rapid progress, developers face critical challenges regarding ethical deployment and algorithmic bias. To mitigate issues like hallucination and ensure factual grounding, the industry is increasingly adopting Retrieval-Augmented Generation (RAG) frameworks."
        elif "summarize the following text" in prompt_lower:
            return "AI transforms industries but raises ethical/bias concerns. RAG is used to improve factual accuracy and reduce hallucinations."
        return "Generic LLM Response"

class SummarizationPipeline:
    def __init__(self, use_mock: bool = True):
        self.use_mock = use_mock
        self.llm = MockLLM()

    def single_prompt_summary(self, text: str) -> str:
        prompt = f"Summarize the following text:\n\n{text}"
        return self.llm.generate(prompt)

    def extract_facts(self, text: str) -> str:
        prompt = f"Extract the most important key facts from the following text as a bulleted list:\n\n{text}"
        return self.llm.generate(prompt)

    def generate_draft(self, facts: str) -> str:
        prompt = f"Using the following key facts, generate a structured summary with paragraphs:\n\n{facts}"
        return self.llm.generate(prompt)

    def refine_summary(self, draft: str) -> str:
        prompt = f"Improve and refine the following summary for better flow, vocabulary, and professional tone:\n\n{draft}"
        return self.llm.generate(prompt)

    def chained_summary(self, text: str) -> dict:
        print("Step 1: Extracting facts...")
        facts = self.extract_facts(text)
        
        print("Step 2: Generating initial draft...")
        draft = self.generate_draft(facts)
        
        print("Step 3: Refining summary...")
        final_summary = self.refine_summary(draft)
        
        return {
            "facts": facts,
            "draft": draft,
            "final": final_summary
        }
