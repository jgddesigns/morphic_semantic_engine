from mse.core import MorphicSemanticEngine


def test_vocab_usage():
    seed = [9, 9, 9, 9, 9, 9, 9, 9, 9]
    vocab = ["X", "Y", "Z"]
    engine = MorphicSemanticEngine(
        initial_state=seed,
        vocab=vocab,
        constants={"a": 2, "b": 3, "c": 1, "d": 4},
        mod=101,
    )
    tokens = engine.generate_tokens(30)
    # All tokens must be drawn from vocab
    assert set(tokens).issubset(set(vocab))
