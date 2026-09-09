import time

class MockFineTuner:
    """Mock implementation of a PEFT/LoRA fine-tuning process."""
    
    def __init__(self):
        self.dataset = [
            {"instruction": "Write a medical summary.", "output": "Patient presents with acute pharyngitis..."},
            {"instruction": "Diagnose based on symptoms.", "output": "Symptoms suggest upper respiratory infection..."}
        ]

    def prepare_dataset(self):
        print("[Step 1] Loading and tokenizing domain-specific dataset...")
        time.sleep(0.5)
        print(f"  -> Loaded {len(self.dataset)} medical examples.")

    def configure_lora(self):
        print("\n[Step 2] Configuring LoRA (Low-Rank Adaptation) adapters...")
        time.sleep(0.5)
        print("  -> Target modules: ['q_proj', 'v_proj']")
        print("  -> Rank (r): 8")
        print("  -> Alpha: 16")

    def train(self):
        print("\n[Step 3] Starting Training Loop...")
        for epoch in range(1, 4):
            time.sleep(0.8)
            loss = 2.5 / epoch
            print(f"  -> Epoch {epoch}/3 | Loss: {loss:.4f}")
        print("  -> Training complete. Adapters saved to ./models/lora-medical")

    def evaluate(self, query: str):
        print(f"\n[Step 4] Evaluating Model on: '{query}'")
        print("  -> Base Model Output: 'I am not a doctor. I cannot provide medical advice.'")
        time.sleep(0.5)
        print("  -> Fine-Tuned Model Output: 'Patient requires rest and hydration. Symptoms align with common viral pharyngitis.'")

    def run_pipeline(self):
        self.prepare_dataset()
        self.configure_lora()
        self.train()
        self.evaluate("Write a medical summary based on a sore throat.")
