from src.vision import MockVisualQASystem

def test_image_retrieval():
    system = MockVisualQASystem()
    res = system.retrieve_image("car")
    assert res["file"] == "car.jpg"

def test_visual_qa():
    system = MockVisualQASystem()
    img = system.retrieve_image("dog")
    ans = system.visual_qa(img, "What color is it?")
    assert "golden" in ans.lower()
