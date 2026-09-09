from src.pipeline import SummarizationPipeline

def test_single_prompt():
    pipeline = SummarizationPipeline(use_mock=True)
    res = pipeline.single_prompt_summary("Test text")
    assert "AI transforms industries" in res

def test_chained_prompt():
    pipeline = SummarizationPipeline(use_mock=True)
    res = pipeline.chained_summary("Test text")
    assert "facts" in res
    assert "draft" in res
    assert "final" in res
    assert "AI is transforming industries" in res["facts"]
    assert "Retrieval-Augmented Generation" in res["final"]
