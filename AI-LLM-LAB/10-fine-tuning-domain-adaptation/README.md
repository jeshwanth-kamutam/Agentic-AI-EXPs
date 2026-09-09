# Experiment 10 — Fine-Tuning for Domain Adaptation

## Objective
Demonstrate the workflow for adapting a base Large Language Model to a specific domain (e.g., Medical or Legal) using Parameter-Efficient Fine-Tuning (PEFT) techniques like LoRA.

## Problem Statement
Base models are trained on general internet data. They often refuse to answer specialized questions (like medical diagnoses) or format them incorrectly. Prompting can help, but fine-tuning embeds the domain knowledge and tone directly into the model weights.

## Technologies Used
* Python
* Hugging Face Transformers (Conceptual)
* PEFT / LoRA (Conceptual)

## Architecture
```text
Base Model + Domain Dataset -> LoRA Adapter Training -> Fine-Tuned Model -> Evaluation
```

## Folder Structure
* `src/`: Core logic (`finetuner.py`)
* `models/`: Directory where trained adapters would be saved
* `tests/`: Pytest suite
* `run.py`: Entry point

## Installation
```bash
pip install -r requirements.txt
```

## Configuration
This experiment runs as a conceptual simulation to avoid requiring a GPU. Copy `.env.example` to `.env`.

## How to Run
```bash
python run.py
```

## Sample Output
```text
[Step 1] Loading and tokenizing domain-specific dataset...
  -> Loaded 2 medical examples.

[Step 2] Configuring LoRA (Low-Rank Adaptation) adapters...
  -> Target modules: ['q_proj', 'v_proj']
  -> Rank (r): 8
  -> Alpha: 16

[Step 3] Starting Training Loop...
  -> Epoch 1/3 | Loss: 2.5000
  -> Epoch 2/3 | Loss: 1.2500
  -> Epoch 3/3 | Loss: 0.8333
  -> Training complete. Adapters saved to ./models/lora-medical

[Step 4] Evaluating Model on: 'Write a medical summary based on a sore throat.'
  -> Base Model Output: 'I am not a doctor. I cannot provide medical advice.'
  -> Fine-Tuned Model Output: 'Patient requires rest and hydration. Symptoms align with common viral pharyngitis.'
```

## Explanation
Instead of training all billions of parameters of an LLM (Full Fine-Tuning), LoRA injects small trainable rank-decomposition matrices into the model's layers. This allows fine-tuning on consumer hardware while keeping the base model frozen.

## Results
The fine-tuned model adopts the tone and format of the domain dataset, whereas the base model either refuses or answers too generically.

## Key Concepts Learned
- Parameter-Efficient Fine-Tuning (PEFT)
- LoRA (Low-Rank Adaptation)
- Dataset Formatting for Instruction Tuning

## Limitations
- This script is a simulation. Real fine-tuning requires significant VRAM (GPU).

## Future Improvements
- Integrate `Unsloth` or `trl` (Transformer Reinforcement Learning) to run a real, lightweight fine-tuning job on a tiny model like `TinyLlama-1.1B`.
