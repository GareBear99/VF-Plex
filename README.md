# VocalForge PersonaPlex Lab

**VocalForge PersonaPlex Lab** is a GitHub-ready starter repo for building a **JUCE plugin + local backend + HTML tester** around [NVIDIA PersonaPlex](https://github.com/NVIDIA/personaplex), aimed at **voice-conditioned vocal asset generation**, **spoken hook design**, **whispers**, **chants**, **robotic/system phrases**, and **sample-pack export**.

It is designed around one hard rule:

> **Never run PersonaPlex inference on the plugin audio thread.**

Instead, this repo separates concerns cleanly:

- **JUCE plugin** for DAW-side control, auditioning, and export workflow
- **Python backend bridge** for queued jobs, health checks, and filesystem outputs
- **HTML tester** for fast iteration outside the DAW
- **PersonaPlex dependency layer** tracked separately through upstream or your fork

## Why this repo exists

NVIDIA PersonaPlex is a real-time, full-duplex speech-to-speech conversational model with **text-based role prompts** and **audio-based voice conditioning**. It supports a fixed set of NAT and VAR voice prompts, a local server mode, and an offline WAV-in/WAV-out path. The upstream code is MIT licensed, while the model weights are released under the NVIDIA Open Model License. citeturn909810view0

That makes PersonaPlex a strong foundation for a **vocal phrase forge**, but not something you should bolt directly into a DAW's audio callback. This repository gives you the product shell around it.

## Product framing

Best framing for this project:

- AI vocal phrase generator
- vocal sample pack builder
- whisper / chant / spoken phrase lab
- offline voice-conditioned export tool
- JUCE + browser control surface for local voice generation

Not the best framing yet:

- live note-played vocal synth
- transparent replacement for human singers
- real-time sample-accurate instrument engine

## Upstream PersonaPlex facts this repo builds around

Upstream PersonaPlex provides:

- a **local HTTPS server** launched with `python -m moshi.server --ssl ...`
- an **offline evaluator** launched with `python -m moshi.offline`
- fixed **voice prompt IDs** including NATF/NATM/VARF/VARM sets
- support for **HF_TOKEN** after the user accepts the model license on Hugging Face
- optional **CPU offload** via `accelerate`

The upstream README describes PersonaPlex as a real-time, full-duplex speech-to-speech model based on the Moshi architecture and lists the NAT/VAR voice sets and offline/server commands. citeturn909810view0

## Recommended repo strategy

Use this repository as your **main product repo**.

Keep PersonaPlex itself separate:

- use **upstream directly** if you are only consuming it
- use **your fork** if you need engine-level changes
- mount it as a **submodule**, **subtree**, or **local path dependency**

Suggested layout:

```text
VocalForge_PersonaPlex_Lab/
  plugin/                  # JUCE plugin shell
  backend/                 # FastAPI bridge + queue + runners
  tester/                  # HTML frontend tester
  shared/                  # schemas, voice maps, shared metadata
  docs/                    # architecture, packaging, attribution, SEO, roadmap
  scripts/                 # dev helpers, linkage scripts, repo setup
  third_party/
    personaplex/           # optional git submodule / local checkout / your fork
```

## Features in this starter repo

### Included now
- JUCE plugin scaffold with async backend client structure
- FastAPI backend with job queue and placeholder WAV output
- HTML tester that talks to the same backend
- JSON schema and voice mapping starter files
- GitHub templates, issue forms, CI, docs, release notes scaffolding
- clear attribution + dependency strategy for PersonaPlex

### Intended next wiring steps
- replace placeholder generation with real PersonaPlex invocation
- connect plugin UI to waveform preview and local library browser
- add drag-export, batch render, and pack metadata export
- package the backend for Catalina / Windows shipping
- decide on submodule vs fork path for PersonaPlex integration

## Quickstart

### 1) Clone this repo

```bash
git clone <your-repo-url>
cd VocalForge_PersonaPlex_Lab
```

### 2) Add PersonaPlex as a dependency

Option A: local clone/fork placed under `third_party/personaplex`

```bash
git clone https://github.com/NVIDIA/personaplex third_party/personaplex
```

Option B: submodule

```bash
git submodule add https://github.com/NVIDIA/personaplex third_party/personaplex
```

### 3) Set up the backend

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app:app --reload --port 8765
```

### 4) Run the tester

```bash
cd tester
python3 -m http.server 8080
```

### 5) Point the backend runner to PersonaPlex

Edit:

- `backend/runners/personaplex_runner.py`

This is where you can choose one of three integration modes:

- spawn `python -m moshi.offline`
- call a running local PersonaPlex server
- build a thin Python-native wrapper if stable in your environment

## SEO / discoverability targets

This repo is intentionally structured for findability around terms like:

- JUCE AI vocal plugin
- PersonaPlex plugin wrapper
- local voice generation plugin
- AI sample pack generator
- NVIDIA PersonaPlex JUCE integration
- offline vocal phrase generator
- speech-to-speech plugin scaffold
- DAW vocal asset generator

See `docs/seo-keywords.md` for the full keyword map and README strategy.

## Topics to use on GitHub

Recommended topics:

- `juce`
- `vst3`
- `audio-plugin`
- `speech-to-speech`
- `personaplex`
- `moshi`
- `fastapi`
- `html-tester`
- `voice-generation`
- `sample-pack-builder`
- `offline-ai`
- `local-ai`
- `audio-tools`

## Licensing and attribution

This repository contains **your product scaffolding** only.

- Your wrapper/plugin/backend code: choose the license you want for this repo
- NVIDIA PersonaPlex upstream code: MIT license upstream citeturn909810view0
- PersonaPlex model weights: NVIDIA Open Model License upstream citeturn909810view0

Read `docs/upstream-attribution.md` before redistributing any PersonaPlex-linked build or claiming generated-output rights.

## Roadmap

- [x] main repo scaffold
- [x] backend queue and starter endpoints
- [x] HTML tester shell
- [x] JUCE project shell
- [ ] real PersonaPlex runner wiring
- [ ] packaged helper app
- [ ] waveform preview / library browser
- [ ] drag-to-DAW export
- [ ] batch phrase CSV pipeline
- [ ] release binaries and screenshots

## Status

This is a **serious starter repository**, not a finished commercial product. It is intentionally shaped so you can layer PersonaPlex under it cleanly and keep upstream updates manageable.
