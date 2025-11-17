"""Example: use different seeds to personalize output per user."""

from mse.core import MorphicSemanticEngine
from mse.seeds import themed_seed_from_word


def make_engine_for_user(user_id: str) -> MorphicSemanticEngine:
    seed = themed_seed_from_word(user_id, length=9)
    vocab = ["calm", "focus", "energy", "rest", "create", "learn", "move", "pause"]
    engine = MorphicSemanticEngine(
        initial_state=seed,
        vocab=vocab,
        constants={"a": 4, "b": 6, "c": 1, "d": 3},
        mod=5003,
    )
    return engine


def main():
    users = ["alice", "bob", "charlie"]

    for user in users:
        engine = make_engine_for_user(user)
        tokens = engine.generate_tokens(10)
        print(f"User {user} → {tokens}")


if __name__ == "__main__":
    main()
