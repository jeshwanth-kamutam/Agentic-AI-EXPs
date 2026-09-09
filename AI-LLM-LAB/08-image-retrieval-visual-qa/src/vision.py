class MockVisualQASystem:
    """Mock implementation of an Image Retrieval and Visual QA system."""
    
    def __init__(self):
        self.image_database = [
            {"id": "img1", "description": "A red sports car driving on a coastal highway.", "file": "car.jpg"},
            {"id": "img2", "description": "A golden retriever playing with a frisbee in a park.", "file": "dog.jpg"},
            {"id": "img3", "description": "A modern kitchen with stainless steel appliances.", "file": "kitchen.jpg"}
        ]
        
    def retrieve_image(self, query: str) -> dict:
        print(f"\n[Retrieval] Converting query '{query}' to embedding and searching vector index...")
        query_lower = query.lower()
        
        # Mock semantic search
        best_match = None
        if "car" in query_lower or "drive" in query_lower:
            best_match = self.image_database[0]
        elif "dog" in query_lower or "animal" in query_lower:
            best_match = self.image_database[1]
        elif "kitchen" in query_lower or "room" in query_lower:
            best_match = self.image_database[2]
            
        if best_match:
            print(f"  -> Found relevant image: {best_match['file']}")
            return best_match
        
        print("  -> No relevant image found.")
        return {}

    def visual_qa(self, image: dict, question: str) -> str:
        if not image:
            return "No image provided for QA."
            
        print(f"\n[Visual QA] Passing image '{image['file']}' and question '{question}' to Vision Model...")
        
        # Mock vision model analysis based on description
        desc = image["description"].lower()
        question_lower = question.lower()
        
        if "color" in question_lower:
            if "red" in desc: return "The car is red."
            if "golden" in desc: return "The dog is golden."
        elif "what" in question_lower:
            return f"Based on the image, I see: {image['description']}"
            
        return "I am not sure how to answer that based on the image."
