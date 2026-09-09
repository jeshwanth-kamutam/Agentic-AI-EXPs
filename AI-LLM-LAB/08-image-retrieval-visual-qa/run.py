import os
from dotenv import load_dotenv
from src.vision import MockVisualQASystem

def main():
    load_dotenv()
    print("--- 08: Image Retrieval & Visual QA ---")
    
    system = MockVisualQASystem()
    
    print("\n--- Test Case 1 ---")
    query1 = "Find an image of a vehicle"
    img1 = system.retrieve_image(query1)
    ans1 = system.visual_qa(img1, "What color is it?")
    print(f"Answer: {ans1}")
    
    print("\n--- Test Case 2 ---")
    query2 = "Find an image of an animal"
    img2 = system.retrieve_image(query2)
    ans2 = system.visual_qa(img2, "What is happening in the image?")
    print(f"Answer: {ans2}")

if __name__ == "__main__":
    main()
