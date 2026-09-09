# Git Separation Guide

This document explains how to turn each of the 12 laboratory experiments into its own independent GitHub repository.

Because each experiment is entirely self-contained (with its own `README.md`, `requirements.txt`, and code), you can initialize a git repository directly inside the experiment's folder.

## General Process

For any experiment folder, you follow these same 6 steps:

1. Navigate into the folder.
2. Initialize a local git repository.
3. Stage all files (the root `.gitignore` rules apply if copied, or you can copy `.gitignore` into the folder first).
4. Commit the files.
5. Create a new repository on GitHub (without a README or .gitignore).
6. Push the local repository to GitHub.

---

## Commands for Each Experiment

### Experiment 01
```bash
cd 01-text-to-sql-workflow
cp ../.gitignore .
git init
git add .
git commit -m "Add Text-to-SQL laboratory experiment"
git branch -M main
git remote add origin <GITHUB_REPOSITORY_URL_FOR_01>
git push -u origin main
```

### Experiment 02
```bash
cd 02-rag-question-answering
cp ../.gitignore .
git init
git add .
git commit -m "Add RAG Question Answering laboratory experiment"
git branch -M main
git remote add origin <GITHUB_REPOSITORY_URL_FOR_02>
git push -u origin main
```

### Experiment 03
```bash
cd 03-prompt-chaining-summarization
cp ../.gitignore .
git init
git add .
git commit -m "Add Prompt Chaining laboratory experiment"
git branch -M main
git remote add origin <GITHUB_REPOSITORY_URL_FOR_03>
git push -u origin main
```

### Experiment 04
```bash
cd 04-sql-agent-tool-use
cp ../.gitignore .
git init
git add .
git commit -m "Add SQL Agent with Tool Use laboratory experiment"
git branch -M main
git remote add origin <GITHUB_REPOSITORY_URL_FOR_04>
git push -u origin main
```

### Experiment 05
```bash
cd 05-multi-agent-sdr
cp ../.gitignore .
git init
git add .
git commit -m "Add Multi-Agent SDR laboratory experiment"
git branch -M main
git remote add origin <GITHUB_REPOSITORY_URL_FOR_05>
git push -u origin main
```

### Experiment 06
```bash
cd 06-policy-compliance-agent
cp ../.gitignore .
git init
git add .
git commit -m "Add Policy Compliance Agent laboratory experiment"
git branch -M main
git remote add origin <GITHUB_REPOSITORY_URL_FOR_06>
git push -u origin main
```

### Experiment 07
```bash
cd 07-deep-research-agent
cp ../.gitignore .
git init
git add .
git commit -m "Add Deep Research Agent laboratory experiment"
git branch -M main
git remote add origin <GITHUB_REPOSITORY_URL_FOR_07>
git push -u origin main
```

### Experiment 08
```bash
cd 08-image-retrieval-visual-qa
cp ../.gitignore .
git init
git add .
git commit -m "Add Image Retrieval and Visual QA laboratory experiment"
git branch -M main
git remote add origin <GITHUB_REPOSITORY_URL_FOR_08>
git push -u origin main
```

### Experiment 09
```bash
cd 09-reasoning-model-benchmark
cp ../.gitignore .
git init
git add .
git commit -m "Add Reasoning Model Benchmarking laboratory experiment"
git branch -M main
git remote add origin <GITHUB_REPOSITORY_URL_FOR_09>
git push -u origin main
```

### Experiment 10
```bash
cd 10-fine-tuning-domain-adaptation
cp ../.gitignore .
git init
git add .
git commit -m "Add Fine-Tuning Domain Adaptation laboratory experiment"
git branch -M main
git remote add origin <GITHUB_REPOSITORY_URL_FOR_10>
git push -u origin main
```

### Experiment 11
```bash
cd 11-model-optimization
cp ../.gitignore .
git init
git add .
git commit -m "Add Model Optimization laboratory experiment"
git branch -M main
git remote add origin <GITHUB_REPOSITORY_URL_FOR_11>
git push -u origin main
```

### Experiment 12
```bash
cd 12-capstone-agentic-system
cp ../.gitignore .
git init
git add .
git commit -m "Add Capstone Agentic System laboratory experiment"
git branch -M main
git remote add origin <GITHUB_REPOSITORY_URL_FOR_12>
git push -u origin main
```

## Important Note before Pushing
Make sure that your `.gitignore` file correctly ignores `.env`, `__pycache__`, and `models/` as they should **never** be committed to public GitHub repositories.
