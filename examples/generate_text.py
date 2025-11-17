"""Example: generate a short token sequence that can be interpreted as text."""

from mse.core import MorphicSemanticEngine
from mse.seeds import themed_seed_from_word


def main():
    seed = themed_seed_from_word("HISTORICAL", length=9)
    vocab = [
        "the", "old", "city", "river", "tower", "wall", "market", "gate", "people",
        "stone", "dust", "fog", "harbor", "hill", "forest",
    ]
    engine = MorphicSemanticEngine(
        initial_state=seed,
        vocab=vocab,
        constants={"a": 3, "b": 5, "c": 7, "d": 11},
        mod=9973,
    )

    tokens = engine.generate_tokens(60)
    print(" ".join(tokens))


if __name__ == "__main__":
    main()
