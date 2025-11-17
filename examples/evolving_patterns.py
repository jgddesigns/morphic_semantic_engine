"""Example: visualize the evolving pattern of token indices."""

from mse.core import MorphicSemanticEngine
from mse.seeds import fib_seed


def main():
    seed = fib_seed(9)
    vocab = [f"T{i}" for i in range(16)]
    engine = MorphicSemanticEngine(
        initial_state=seed,
        vocab=vocab,
        constants={"a": 2, "b": 7, "c": 1, "d": 9},
        mod=1009,
    )

    for step in range(40):
        token = engine.next_token()
        print(f"{step:02d}: {token}")


if __name__ == "__main__":
    main()
