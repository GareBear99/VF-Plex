# Contributing

## Ground rules
- Keep PersonaPlex as a separate dependency or fork; do not dump upstream into this repo without reason.
- Never place heavyweight inference on the JUCE audio thread.
- Prefer deterministic, inspectable queue-based behavior over silent magic.
- Document any licensing implications when changing PersonaPlex integration.

## Development flow
1. Open an issue describing the change.
2. Keep changes scoped by subsystem: plugin, backend, tester, docs.
3. Include verification notes and screenshots where relevant.
4. Update docs when changing architecture or packaging.

## Code style
- C++: simple, readable JUCE-style code with clear service boundaries.
- Python: typed functions where practical, explicit error messages, minimal hidden state.
- Frontend: plain HTML/CSS/JS unless a framework becomes justified.
