> 🎛️ Part of the [TizWildin Plugin Ecosystem](https://garebear99.github.io/TizWildinEntertainmentHUB/) — 16 free audio plugins with a live update dashboard.
>
> [FreeEQ8](https://github.com/GareBear99/FreeEQ8) · [XyloCore](https://github.com/GareBear99/XyloCore) · [Instrudio](https://github.com/GareBear99/Instrudio) · [Therum](https://github.com/GareBear99/Therum_JUCE-Plugin) · [BassMaid](https://github.com/GareBear99/BassMaid) · [SpaceMaid](https://github.com/GareBear99/SpaceMaid) · [GlueMaid](https://github.com/GareBear99/GlueMaid) · [MixMaid](https://github.com/GareBear99/MixMaid) · [ChainMaid](https://github.com/GareBear99/ChainMaid) · [PaintMask](https://github.com/GareBear99/PaintMask_Free-JUCE-Plugin) · [WURP](https://github.com/GareBear99/WURP_Toxic-Motion-Engine_JUCE) · [AETHER](https://github.com/GareBear99/AETHER_Choir-Atmosphere-Designer) · [WhisperGate](https://github.com/GareBear99/WhisperGate_Free-JUCE-Plugin) · [RiftWave](https://github.com/GareBear99/RiftWaveSuite_RiftSynth_WaveForm_Lite) · [FreeSampler](https://github.com/GareBear99/FreeSampler_v0.3) · [VF-PlexLab](https://github.com/GareBear99/VF-PlexLab) · [PAP-Forge-Audio](https://github.com/GareBear99/PAP-Forge-Audio)
>
> 🎵 [Awesome Audio](https://github.com/GareBear99/awesome-audio-plugins-dev) — (FREE) Awesome Audio Dev List
>
> 🎁 [Free Packs & Samples](#tizwildin-free-sample-packs) — jump to free packs & samples

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

## TizWildin FREE sample packs

| Pack | Description |
|------|-------------|
| [**TizWildin-Aurora**](https://github.com/GareBear99/TizWildin-Aurora) | 3-segment original synth melody pack with loops, stems, demo renders, and neon/cinematic phrasing |
| [**TizWildin-Obsidian**](https://github.com/GareBear99/TizWildin-Obsidian) | Dark cinematic sample pack with choir textures, menu loops, transitions, bass, atmosphere, drums, and electric-banjo extensions |
| [**TizWildin-Skyline**](https://github.com/GareBear99/TizWildin-Skyline) | 30 BPM-tagged synthwave and darkwave loops with generator snapshot and dark neon additions |
| [**TizWildin-Chroma**](https://github.com/GareBear99/TizWildin-Chroma) | Multi-segment game synthwave loop sample pack from TizWildin Entertainment |
| [**TizWildin-Chime**](https://github.com/GareBear99/TizWildin-Chime) | Multi-part 88 BPM chime collection spanning glass, void, halo, reed, and neon synthwave lanes |
| [**Free Violin Synth Sample Kit**](https://github.com/GareBear99/Free-Violin-Synth-Sample-Kit) | Physical-model violin sample kit rendered from the Instrudio violin instrument |
| [**Free Dark Piano Sound Kit**](https://github.com/GareBear99/Free-Dark-Piano-Sound-Kit) | 88 piano notes + dark/cinematic loops and MIDI |
| [**Free 808 Producer Kit**](https://github.com/GareBear99/Free-808-Producer-Kit) | 94 hand-crafted 808 bass samples tuned to every chromatic key |
| [**Free Riser Producer Kit**](https://github.com/GareBear99/Free-Riser-Producer-Kit) | 115+ risers and 63 downlifters - noise, synth, drum, FX, cinematic |
| [**Phonk Producer Toolkit**](https://github.com/GareBear99/Phonk_Producer_Toolkit) | Drift phonk starter kit - 808s, cowbells, drums, MIDI, templates |
| [**Free Future Bass Producer Kit**](https://github.com/GareBear99/Free-Future-Bass-Producer-Kit) | Loops, fills, drums, bass, synths, pads, and FX |

### Related audio projects
- [**VF-PlexLab**](https://github.com/GareBear99/VF-PlexLab) - VocalForge PersonaPlex Lab starter repo for a JUCE plugin + local backend + HTML tester around NVIDIA PersonaPlex.
- [**PAP-Forge-Audio**](https://github.com/GareBear99/PAP-Forge-Audio) - Procedural Autonomous Plugins runtime for generating, branching, validating, and restoring plugin projects from natural-language sound intent.

## TizWildin FREE sample packs

| Pack | Description |
|------|-------------|
| [**TizWildin-Aurora**](https://github.com/GareBear99/TizWildin-Aurora) | 3-segment original synth melody pack with loops, stems, demo renders, and neon/cinematic phrasing |
| [**TizWildin-Obsidian**](https://github.com/GareBear99/TizWildin-Obsidian) | Dark cinematic sample pack with choir textures, menu loops, transitions, bass, atmosphere, drums, and electric-banjo extensions |
| [**TizWildin-Skyline**](https://github.com/GareBear99/TizWildin-Skyline) | 30 BPM-tagged synthwave and darkwave loops with generator snapshot and dark neon additions |
| [**TizWildin-Chroma**](https://github.com/GareBear99/TizWildin-Chroma) | Multi-segment game synthwave loop sample pack from TizWildin Entertainment |
| [**TizWildin-Chime**](https://github.com/GareBear99/TizWildin-Chime) | Multi-part 88 BPM chime collection spanning glass, void, halo, reed, and neon synthwave lanes |
| [**Free Violin Synth Sample Kit**](https://github.com/GareBear99/Free-Violin-Synth-Sample-Kit) | Physical-model violin sample kit rendered from the Instrudio violin instrument |
| [**Free Dark Piano Sound Kit**](https://github.com/GareBear99/Free-Dark-Piano-Sound-Kit) | 88 piano notes + dark/cinematic loops and MIDI |
| [**Free 808 Producer Kit**](https://github.com/GareBear99/Free-808-Producer-Kit) | 94 hand-crafted 808 bass samples tuned to every chromatic key |
| [**Free Riser Producer Kit**](https://github.com/GareBear99/Free-Riser-Producer-Kit) | 115+ risers and 63 downlifters - noise, synth, drum, FX, cinematic |
| [**Phonk Producer Toolkit**](https://github.com/GareBear99/Phonk_Producer_Toolkit) | Drift phonk starter kit - 808s, cowbells, drums, MIDI, templates |
| [**Free Future Bass Producer Kit**](https://github.com/GareBear99/Free-Future-Bass-Producer-Kit) | Loops, fills, drums, bass, synths, pads, and FX |

### Related audio projects
- [**VF-PlexLab**](https://github.com/GareBear99/VF-PlexLab) - VocalForge PersonaPlex Lab starter repo for a JUCE plugin + local backend + HTML tester around NVIDIA PersonaPlex.
- [**PAP-Forge-Audio**](https://github.com/GareBear99/PAP-Forge-Audio) - Procedural Autonomous Plugins runtime for generating, branching, validating, and restoring plugin projects from natural-language sound intent.
