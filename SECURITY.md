# Security Policy

## Supported versions
This repository is pre-1.0 and under active development.

## Reporting a vulnerability
Please avoid posting exploit details in public issues. Report security concerns privately and include:
- affected component
- reproduction steps
- impact assessment
- suggested mitigation if known

## Sensitive areas
- local backend binding and auth assumptions
- filesystem writes / output paths
- subprocess invocation for PersonaPlex
- model / token handling via HF_TOKEN
