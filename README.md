# Morphic Semantic Engine (MSE)

**Big content from small seeds. Deterministic, reproducible, and offline.**


The origin of this idea started with the 'Infinite Map Concept' I created in early 2025. The core logic starts with the idea of using a static length array of numbers which has values that change based on a mathematic function. Data is mapped that can be used based on the state of the morphed array. The single number array is all that is needed to produce a continuing chain of useful output.

This idea was improved upon with some help from ChatGPT, and has become the Morphic Semantic Engine.



The Morphic Semantic Engine (MSE) is a tiny, deterministic generative system that grows complex,
structured output from a small numeric seed. Instead of massive AI models or hand-written rules,
MSE uses a fixed-length array of integers and a simple morphing rule to produce evolving,
semantic sequences you can use for:

- Synthetic data generation
- Deterministic simulations
- Procedural text & lore
- Privacy-safe personalization
- Embedded / offline generative behavior

This repository contains a reference implementation in Python, example scripts, and documentation.

---

## Features

- **Deterministic** – same seed → same output on any machine.
- **Lightweight** – core state is just a handful of integers (< 1 KB).
- **No training** – no datasets, no GPUs, no model weights.
- **Semantic output** – not just random noise; tokens can represent text, events, or structures.
- **Reproducible** – perfect for QA, research, and simulation replays.
- **Offline-friendly** – runs on laptops, servers, and small embedded devices.

---

## How It Works (High-Level)

1. **Seed** – You start with a small fixed-length array of integers (e.g. 9 numbers).
2. **Morph Rule** – On each step, the array is updated using a deterministic formula that
   combines the current value, a neighbor, and the iteration index.
3. **Code Extraction** – The engine summarizes the state into a small integer "code"
   using weighted sums and offsets.
4. **Semantic Mapping** – The code is mapped into a vocabulary index, producing a token.
5. **Feedback** – The previously chosen token influences the next mapping, so the "meaning"
   evolves with the state.

The result is a compact engine that turns tiny seeds into large, evolving sequences that feel
structured and consistent over time.

---

## Use Cases

### Synthetic Data

Generate large, reproducible datasets (e.g. sensor readings, event streams, synthetic markets)
from a single small seed. This avoids privacy issues and reduces cost compared to collecting
real-world data.

See: [`examples/synthetic_data.py`](examples/synthetic_data.py)

### Deterministic Simulations

Use the engine as a core "randomness" and structure driver for simulations where you need
perfect replayability. A saved seed + step index can reconstruct entire runs.

See: [`examples/reproducible_simulation.py`](examples/reproducible_simulation.py)

### Procedural Text & Lore

Create lightweight procedural text: short lore snippets, logs, histories, and flavor text
without machine learning models.

See: [`examples/generate_text.py`](examples/generate_text.py)

### Personalization Without Storing User Data

Assign each user a seed and derive their long-term content pattern from it, without storing
behavioral data or personally identifiable information.

See: [`examples/seed_personalization.py`](examples/seed_personalization.py)

---

## Project Structure

```text
morphic-semantic-engine/
├── src/
│   └── mse/
│       ├── __init__.py
│       ├── core.py
│       ├── morph_rules.py
│       ├── semantic_mapper.py
│       └── seeds.py
├── examples/
│   ├── generate_text.py
│   ├── synthetic_data.py
│   ├── evolving_patterns.py
│   ├── seed_personalization.py
│   └── reproducible_simulation.py
├── docs/
│   ├── design_overview.md
│   ├── math_details.md
│   ├── api_reference.md
│   └── seeds_catalog.md
├── tests/
│   ├── test_core.py
│   ├── test_determinism.py
│   └── test_semantics.py
├── web_demo/
│   ├── index.html
│   ├── mse.js
│   └── demo_styles.css
├── LICENSE
├── CONTRIBUTING.md
├── CHANGELOG.md
├── setup.py
├── requirements.txt
└── .gitignore
```

---



## Contributing

Contributions, ideas, and experiments are welcome!

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for guidelines.

---

## License

This project is released under the MIT License. See [`LICENSE`](LICENSE) for details.

If you use this in research, products, or experiments, a mention or citation of the
"Morphic Semantic Engine" is appreciated.
