// Minimal JS demo version: not a full port, just a flavor demo.

function themedSeedFromWord(word, length = 9) {
  word = (word || "").toUpperCase();
  const base = [];
  for (const ch of word) {
    if (/[A-Z]/.test(ch)) {
      const v = ch.charCodeAt(0) - 64;
      base.push(Math.max(1, Math.min(26, v)));
    }
  }
  if (base.length === 0) base.push(1);
  const out = [];
  let i = 0;
  while (out.length < length) {
    out.push(base[i % base.length]);
    i++;
  }
  return out.slice(0, length);
}

function morphStateDefault(state, t, mod, a, b, c, d) {
  const n = state.length;
  const res = new Array(n);
  for (let i = 0; i < n; i++) {
    const left = state[(i - 1 + n) % n];
    const center = state[i];
    res[i] = (a * center + b * left + c * t + d) % mod;
  }
  return res;
}

class MorphicSemanticEngineJS {
  constructor(initialState, vocab, constants, mod = 9973) {
    this.state = initialState.map(x => ((x % mod) + mod) % mod);
    this.vocab = vocab.slice();
    this.mod = mod;
    this.t = 0;
    this.a = constants.a ?? 3;
    this.b = constants.b ?? 5;
    this.c = constants.c ?? 7;
    this.d = constants.d ?? 11;
    this.prevIndex = 0;
  }

  baseCode() {
    let total = 0;
    for (let i = 0; i < this.state.length; i++) {
      total += (i + 1) * this.state[i];
    }
    return (total + this.t) % 27;
  }

  offset() {
    const sum = this.state.reduce((acc, v) => acc + v, 0);
    return sum % this.vocab.length;
  }

  nextToken() {
    const base = this.baseCode();
    const offs = this.offset();
    const idx = (base + offs + this.prevIndex) % this.vocab.length;
    this.prevIndex = idx;
    const token = this.vocab[idx];

    this.state = morphStateDefault(this.state, this.t, this.mod, this.a, this.b, this.c, this.d);
    this.t += 1;
    return token;
  }
}

window.addEventListener("DOMContentLoaded", () => {
  const seedInput = document.getElementById("seedInput");
  const runBtn = document.getElementById("runBtn");
  const output = document.getElementById("output");

  runBtn.addEventListener("click", () => {
    const word = seedInput.value || "HISTORICAL";
    const seed = themedSeedFromWord(word, 9);
    const vocab = [
      "the", "old", "city", "river", "tower", "wall", "market", "gate", "people",
      "stone", "dust", "fog", "harbor", "hill", "forest",
    ];
    const engine = new MorphicSemanticEngineJS(seed, vocab, {a:3,b:5,c:7,d:11}, 9973);

    const tokens = [];
    for (let i = 0; i < 40; i++) {
      tokens.push(engine.nextToken());
    }
    output.textContent = tokens.join(" ");
  });
});
