from mse.core import MorphicSemanticEngine


def test_engine_runs():
    seed = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    vocab = ["A", "B", "C"]
    engine = MorphicSemanticEngine(
        initial_state=seed,
        vocab=vocab,
        constants={"a": 3, "b": 5, "c": 7, "d": 11},
        mod=9973,
    )
    tokens = engine.generate_tokens(10)
    assert len(tokens) == 10
