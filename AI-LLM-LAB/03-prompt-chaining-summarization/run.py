import os
from dotenv import load_dotenv
from src.pipeline import SummarizationPipeline

def main():
    load_dotenv()
    use_mock = os.getenv("MOCK_LLM", "true").lower() == "true"
    
    print("--- 03: Prompt Chaining for Summarization ---")
    
    sample_text = """
    Artificial Intelligence is rapidly changing how we work and live. From automating mundane tasks in manufacturing to assisting doctors in diagnosing diseases, the impact is undeniable. However, this rapid growth brings significant challenges. AI models can inherit biases from their training data, leading to unfair outcomes. Furthermore, large language models are known to 'hallucinate' or make up facts. To combat this, researchers are developing frameworks like Retrieval-Augmented Generation (RAG) which forces the AI to look up factual information before answering, thereby improving reliability.
    """
    
    pipeline = SummarizationPipeline(use_mock=use_mock)
    
    print("\n=== APPROACH 1: Single Prompt Summarization ===")
    single_result = pipeline.single_prompt_summary(sample_text)
    print(single_result)
    
    print("\n=== APPROACH 2: Multi-Step Prompt Chaining ===")
    chained_results = pipeline.chained_summary(sample_text)
    
    print("\n[Intermediate] Facts Extracted:")
    print(chained_results["facts"])
    
    print("\n[Intermediate] Draft Generated:")
    print(chained_results["draft"])
    
    print("\n[Final] Refined Summary:")
    print(chained_results["final"])

    print("\n=== COMPARISON ===")
    print("The single prompt is often shorter and more generic.")
    print("The chained approach allows the LLM to focus on extraction first, structuring second, and polishing third, leading to a much higher quality output.")

if __name__ == "__main__":
    main()
