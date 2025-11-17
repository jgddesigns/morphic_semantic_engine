"""Example: demonstrate deterministic replay using the same seed and steps."""

from mse.core import MorphicSemanticEngine
from mse.seeds import fib_seed


def build_engine():
    seed = fib_seed(9)
    vocab = ["A", "B", "C", "D", "E"]
    engine = MorphicSemanticEngine(
        initial_state=seed,
        vocab=vocab,
        constants={"a": 3, "b": 5, "c": 7, "d": 11},
        mod=9973,
    )
    return engine


def run_simulation(steps: int):
    engine = build_engine()
    sequence = []
    for _ in range(steps):
        sequence.append(engine.next_token())
    return sequence


def main():
    seq1 = run_simulation(20)
    seq2 = run_simulation(20)
    print("First run :", seq1)
    print("Second run:", seq2)
    print("Identical? ", seq1 == seq2)


if __name__ == "__main__":
    main()
