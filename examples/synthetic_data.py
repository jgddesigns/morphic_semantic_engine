"""Example: use MSE to drive a synthetic data stream."""

import random
from mse.core import MorphicSemanticEngine
from mse.seeds import fib_seed


def main():
    seed = fib_seed(9)
    vocab = list(range(10))  # numeric tokens 0..9
    engine = MorphicSemanticEngine(
        initial_state=seed,
        vocab=[str(v) for v in vocab],
        constants={"a": 5, "b": 3, "c": 2, "d": 1},
        mod=10007,
    )

    print("timestamp,value")
    t = 0
    for _ in range(100):
        token = engine.next_token()
        value = int(token)
        # small random jitter layered on top of deterministic core if desired
        noisy_value = value + random.randint(-1, 1)
        print(f"{t},{noisy_value}")
        t += 1


if __name__ == "__main__":
    main()
