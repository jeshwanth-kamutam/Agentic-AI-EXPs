# Experiment 08 — Image Retrieval / Visual QA System

## Objective
Build a multimodal AI pipeline that retrieves a relevant image based on a text query and then answers questions about that specific image using a Vision Model.

## Problem Statement
Standard RAG systems only operate on text. To interact with visual data, the system must project images and text into the same vector space for retrieval, and then use a Multimodal LLM to analyze the image content.

## Technologies Used
* Python
* Multimodal Vector Search Simulation
* Vision-Language Model Simulation

## Architecture
```text
Image Dataset -> Image Representation (Embeddings) -> Vector Index
Query -> Retrieve Relevant Image -> Vision Model + Question -> Answer
```

## Folder Structure
* `src/`: Core logic (`vision.py`)
* `tests/`: Pytest suite
* `run.py`: Entry point

## Installation
```bash
pip install -r requirements.txt
```

## Configuration
Copy `.env.example` to `.env`. Uses a mock multimodal setup by default to avoid the need for heavy local vision models (like LLaVA) or expensive APIs (like GPT-4V).

## How to Run
```bash
python run.py
```

## Sample Input
```text
Retrieval Query: "Find an image of a vehicle"
QA Query: "What color is it?"
```

## Sample Output
```text
[Retrieval] Converting query 'Find an image of a vehicle' to embedding and searching vector index...
  -> Found relevant image: car.jpg

[Visual QA] Passing image 'car.jpg' and question 'What color is it?' to Vision Model...
Answer: The car is red.
```

## Explanation
First, the system simulates converting a text query into a multimodal embedding (e.g. CLIP) to search a database of image embeddings. Once the relevant image is found, it is passed along with the user's question to a Vision Language Model (VLM), which "looks" at the image to provide an answer.

## Results
The system seamlessly transitions from text-based retrieval to visual analysis.

## Key Concepts Learned
- Multimodal Embeddings (e.g., CLIP, SigLIP)
- Vision Language Models (VLMs)
- Cross-modal retrieval

## Limitations
- This is a mock simulation. Real visual retrieval requires a model like CLIP to generate embeddings.
- Real VLMs require significant GPU memory.

## Future Improvements
- Integrate `transformers` with a lightweight model like `Salesforce/blip-image-captioning-base` to perform real visual QA.
