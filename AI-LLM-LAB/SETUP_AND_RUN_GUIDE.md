# Setup and Execution Guide

This document explains what you need to fill out before running the experiments and provides the exact commands to install and run each of the 12 laboratory experiments.

---

## 1. Things You Need to Fill In (Environment Variables)

By default, every experiment is configured to run in **MOCK MODE**. This means you do **not** need to fill in anything to get them to run initially—they will simulate the AI responses so you can verify the code works without paying for an API.

If you want to use a real Large Language Model (like OpenAI's GPT-4) instead of the mock simulation, you must do the following for the specific experiment folder:

1. Copy the `.env.example` file and rename it to `.env`.
2. Open the new `.env` file.
3. Change `MOCK_LLM=true` to `MOCK_LLM=false`.
4. Fill in your API key where it says `OPENAI_API_KEY=your_api_key`.

*(Note: Experiment 10 also mentions a `HF_TOKEN` for Hugging Face if you plan to download gated models in a real fine-tuning scenario.)*

---

## 2. How to Install and Run Each Experiment

You must create a virtual environment or simply install the dependencies directly. It is recommended to use a virtual environment. 

For **every** experiment, the general pattern is:
1. Open a terminal.
2. `cd` into the experiment folder.
3. Run `pip install -r requirements.txt`.
4. Run `python run.py`.

Here are the exact commands for all 12 experiments. You can copy and paste these blocks directly into your terminal.

### Experiment 01: Text-to-SQL Workflow
```bash
cd AI-LLM-LAB/01-text-to-sql-workflow
pip install -r requirements.txt
python run.py
```

### Experiment 02: RAG Question Answering
```bash
cd AI-LLM-LAB/02-rag-question-answering
pip install -r requirements.txt
python run.py
```

### Experiment 03: Prompt Chaining Summarization
```bash
cd AI-LLM-LAB/03-prompt-chaining-summarization
pip install -r requirements.txt
python run.py
```

### Experiment 04: SQL Agent with Tool Use
```bash
cd AI-LLM-LAB/04-sql-agent-tool-use
pip install -r requirements.txt
python run.py
```

### Experiment 05: Multi-Agent SDR System
```bash
cd AI-LLM-LAB/05-multi-agent-sdr
pip install -r requirements.txt
python run.py
```

### Experiment 06: Policy Compliance Agent
```bash
cd AI-LLM-LAB/06-policy-compliance-agent
pip install -r requirements.txt
python run.py
```

### Experiment 07: Deep Research Agent
```bash
cd AI-LLM-LAB/07-deep-research-agent
pip install -r requirements.txt
python run.py
```

### Experiment 08: Image Retrieval / Visual QA
```bash
cd AI-LLM-LAB/08-image-retrieval-visual-qa
pip install -r requirements.txt
python run.py
```

### Experiment 09: Reasoning Model Benchmark
```bash
cd AI-LLM-LAB/09-reasoning-model-benchmark
pip install -r requirements.txt
python run.py
```

### Experiment 10: Fine-Tuning Domain Adaptation
```bash
cd AI-LLM-LAB/10-fine-tuning-domain-adaptation
pip install -r requirements.txt
python run.py
```

### Experiment 11: Model Optimization
```bash
cd AI-LLM-LAB/11-model-optimization
pip install -r requirements.txt
python run.py
```

### Experiment 12: Capstone Agentic System
```bash
cd AI-LLM-LAB/12-capstone-agentic-system
pip install -r requirements.txt
python run.py
```

---

## 3. How to Run the Tests

If you want to run the automated tests (`pytest`) for an experiment to verify its logic, navigate to the folder and run:

```bash
cd AI-LLM-LAB/<experiment-folder-name>
python -m pytest tests/
```
