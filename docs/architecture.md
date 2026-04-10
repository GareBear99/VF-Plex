# Architecture

## Core separation

This project is deliberately split into four layers:

1. **Plugin layer** — JUCE UI, queue submission, preview, export UX.
2. **Backend layer** — job orchestration, PersonaPlex invocation, local filesystem outputs.
3. **Tester layer** — browser-first iteration surface using the same backend.
4. **Dependency layer** — upstream PersonaPlex checkout or your fork.

## Why separate PersonaPlex

NVIDIA PersonaPlex already exposes server and offline execution paths. The cleanest product architecture is to wrap those paths rather than merge upstream internals directly into the plugin shell. This keeps updates, attribution, and troubleshooting manageable. Upstream documents both `python -m moshi.server` and `python -m moshi.offline` usage. citeturn909810view0

## Audio-thread safety doctrine

- No model inference on the real-time callback.
- No blocking disk/network/model startup calls from DSP.
- Plugin talks to backend asynchronously.
- Backend writes explicit job state and output paths.
