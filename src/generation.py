import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

def get_llm():
    """Initializes the LLM (Groq)."""
    groq_api_key = os.environ.get("GROQ_API_KEY")
    if not groq_api_key:
        raise ValueError("GROQ_API_KEY environment variable not found.")
    
    llm = ChatGroq(
        temperature=0, 
        groq_api_key=groq_api_key, 
        model_name="llama3-8b-8192"
    )
    return llm

def get_prompt_template():
    """Returns the prompt template for RAG."""
    template = """Use the following pieces of retrieved context to answer the question. 
If you don't know the answer, just say that you don't know. 
Use three sentences maximum and keep the answer concise.

Context:
{context}

Question: {question}

Answer:"""
    return PromptTemplate.from_template(template)
