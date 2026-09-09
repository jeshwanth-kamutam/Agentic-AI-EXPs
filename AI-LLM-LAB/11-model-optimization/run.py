import os
from dotenv import load_dotenv
from src.optimizer import MockQuantizer

def main():
    load_dotenv()
    print("--- 11: Model Optimization (Quantization) ---")
    
    optimizer = MockQuantizer()
    
    # Simulate quantization from FP32 to INT8
    optimizer.optimize(base_format="fp32", target_format="int8")
    
    # Simulate aggressive quantization to INT4
    optimizer.optimize(base_format="fp16", target_format="int4")

if __name__ == "__main__":
    main()
