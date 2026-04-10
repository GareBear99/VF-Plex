from __future__ import annotations

import json
import math
import os
import struct
import subprocess
import wave
from pathlib import Path
from typing import Iterable, Tuple


def _safe_slug(text: str) -> str:
    out = "".join(ch.lower() if ch.isalnum() else "_" for ch in text.strip())
    while "__" in out:
        out = out.replace("__", "_")
    return out.strip("_")[:48] or "sample"


def _write_placeholder_wav(path: Path, seconds: float, seed: int) -> None:
    sample_rate = 24000
    frames = max(1, int(seconds * sample_rate))
    amplitude = 8000
    freq = 180 + (seed % 220)
    path.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(path), "w") as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(sample_rate)
        for i in range(frames):
            t = i / sample_rate
            env = min(1.0, t * 8.0) * min(1.0, (seconds - t) * 8.0 if seconds > t else 0.0)
            value = int(amplitude * env * math.sin(2.0 * math.pi * freq * t))
            wav.writeframesraw(struct.pack("<h", value))


def _personaplex_root() -> Path | None:
    env_root = os.getenv("PERSONAPLEX_ROOT", "").strip()
    if not env_root:
        return None
    path = Path(env_root)
    return path if path.exists() else None


def _build_offline_command(personaplex_root: Path, voice_id: str, prompt_text: str, input_wav: Path, output_wav: Path, output_json: Path, seed: int) -> list[str]:
    voice_prompt = f"{voice_id}.pt"
    return [
        "python",
        "-m",
        "moshi.offline",
        "--voice-prompt",
        voice_prompt,
        "--text-prompt",
        prompt_text,
        "--input-wav",
        str(input_wav),
        "--seed",
        str(seed),
        "--output-wav",
        str(output_wav),
        "--output-text",
        str(output_json),
    ]


def run_generation(
    prompt_text: str,
    voice_id: str,
    seed: int,
    target_seconds: float,
    category: str,
    output_dir: str,
    style_tags: Iterable[str] | None = None,
) -> Tuple[str, str]:
    """
    Generation runner.

    Current behavior:
    - writes a placeholder WAV so the repo is testable end-to-end immediately
    - writes a sidecar metadata JSON for later indexing

    Upgrade path:
    - if PERSONAPLEX_ROOT is set and you want real integration, replace the
      placeholder block with a subprocess call into PersonaPlex offline mode
      or a local API call to a running PersonaPlex server.
    """
    slug = _safe_slug(prompt_text)
    filename = f"{category}_{voice_id}_{seed}_{slug}.wav"
    output_path = Path(output_dir) / category / filename
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Placeholder implementation for repo validation.
    _write_placeholder_wav(output_path, target_seconds, seed)

    metadata = {
        "prompt_text": prompt_text,
        "voice_id": voice_id,
        "seed": seed,
        "target_seconds": target_seconds,
        "category": category,
        "style_tags": list(style_tags or []),
        "output_file": str(output_path.resolve()),
        "personaplex_root": str(_personaplex_root()) if _personaplex_root() else None,
        "integration_note": "Replace placeholder generation with real PersonaPlex wiring when ready.",
    }
    output_path.with_suffix('.json').write_text(json.dumps(metadata, indent=2))
    return filename, str(output_path.resolve())
