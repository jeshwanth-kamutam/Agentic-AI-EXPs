from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

from src.retrieval import get_vectorstore, get_retriever
from src.generation import get_llm, get_prompt_template

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def setup_rag_chain(persist_directory="./chroma_db"):
    """Sets up the Retrieval-Augmented Generation chain."""
    # 1. Setup Retrieval
    vectorstore = get_vectorstore(persist_directory)
    retriever = get_retriever(vectorstore)
    
    # 2. Setup Generation
    llm = get_llm()
    prompt = get_prompt_template()
    
    # 3. Create Chain
    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    return rag_chain

def ask_question(rag_chain, question):
    return rag_chain.invoke(question)
