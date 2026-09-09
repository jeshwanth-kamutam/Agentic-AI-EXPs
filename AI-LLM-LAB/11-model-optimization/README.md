# Experiment 11 — Model Optimization Experiment

## Objective
Demonstrate the effects of Model Quantization on model size, inference latency, and accuracy.

## Problem Statement
Deploying Large Language Models requires massive memory (VRAM) and compute power. A 7B parameter model in 32-bit floating-point requires ~28GB of VRAM just to load. Quantization reduces the precision of the model weights, allowing it to run on consumer hardware at the cost of a slight accuracy drop.

## Technologies Used
* Python
* Quantization concepts (FP32, FP16, INT8, INT4)

## Architecture
```text
Original Model (FP32) -> Quantization (Scaling factors applied) -> Optimized Model (INT8) -> Benchmark
```

## Folder Structure
* `src/`: Core logic (`optimizer.py`)
* `tests/`: Pytest suite
* `run.py`: Entry point

## Installation
```bash
pip install -r requirements.txt
```

## Configuration
Copy `.env.example` to `.env`. This script uses a mock simulation to explain the concepts without requiring gigabytes of model downloads.

## How to Run
```bash
python run.py
```

## Sample Output
```text
[Optimization] Quantizing model from fp32 to int8...
  -> Calculating scaling factors...
  -> Applying weight quantization...

=== Quantization Report ===
Format:       FP32 -> INT8
Model Size:   14.0 GB -> 3.5 GB (4.0x smaller)
Latency:      120 ms -> 40 ms (3.0x faster)
Accuracy:     95.5% -> 94.1%
```

## Explanation
Quantization maps high-precision float values (e.g., 32-bit) into lower-precision integers (e.g., 8-bit). The script simulates this process, showing how moving from FP32 to INT8 drastically reduces size and latency while only slightly reducing accuracy.

## Results
The optimized INT8 model is 4x smaller and 3x faster, making it viable for edge deployment.

## Key Concepts Learned
- Model Quantization (INT8, INT4)
- Trade-offs in model deployment (Size/Speed vs. Accuracy)

## Limitations
- This is a simulation. Real quantization uses tools like `llama.cpp` (GGUF format) or AutoGPTQ.

## Future Improvements
- Integrate `llama.cpp` python bindings to load a real GGUF model and measure actual tokens/second generation speed.
