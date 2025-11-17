# API Reference

## `MorphicSemanticEngine`

```python
from mse.core import MorphicSemanticEngine
```

### Constructor

```python
MorphicSemanticEngine(
    initial_state: Sequence[int],
    vocab: Sequence[str],
    constants: Dict[str, int],
    mod: int = 9973,
)
```

- `initial_state`: list/sequence of integers (your seed).
- `vocab`: list of tokens (strings) to emit.
- `constants`: dict with keys `"a"`, `"b"`, `"c"`, `"d"` controlling the morph.
- `mod`: modulus for internal arithmetic.

### Methods

- `next_token() -> str`  
  Advance one step and return the next token.

- `generate_tokens(n: int) -> List[str]`  
  Generate a list of `n` tokens by repeated stepping.
