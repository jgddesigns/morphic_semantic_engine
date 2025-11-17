from mse.core import MorphicSemanticEngine


def build():
    seed = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    vocab = ["A", "B", "C", "D"]
    return MorphicSemanticEngine(
        initial_state=seed,
        vocab=vocab,
        constants={"a": 3, "b": 5, "c": 7, "d": 11},
        mod=9973,
    )


def test_deterministic_sequence():
    e1 = build()
    e2 = build()
    seq1 = e1.generate_tokens(50)
    seq2 = e2.generate_tokens(50)
    assert seq1 == seq2
