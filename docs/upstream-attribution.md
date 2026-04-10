# Upstream Attribution

This project is a wrapper/scaffold around NVIDIA PersonaPlex.

## Upstream repository
- NVIDIA PersonaPlex: https://github.com/NVIDIA/personaplex

## What upstream provides
The upstream repository provides PersonaPlex code, including local server usage, offline WAV evaluation, voice prompt IDs, and installation guidance. It describes PersonaPlex as a real-time, full-duplex speech-to-speech conversational model based on the Moshi architecture and states that the code is MIT licensed while the weights are under the NVIDIA Open Model License. citeturn909810view0

## What this repository provides
- JUCE wrapper/plugin shell
- backend bridge and queue management
- browser tester
- packaging/docs/repo scaffolding

## Important note
Do not imply that this repository owns or relicenses PersonaPlex itself. Keep upstream notices intact and review model-weight terms before shipping binaries that bundle or automate model downloads.
