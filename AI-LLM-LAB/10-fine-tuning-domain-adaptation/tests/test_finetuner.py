from src.finetuner import MockFineTuner

def test_dataset_load():
    finetuner = MockFineTuner()
    assert len(finetuner.dataset) == 2
    assert "instruction" in finetuner.dataset[0]
