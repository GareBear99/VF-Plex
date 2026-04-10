# Packaging Notes

## Shipping shape

Recommended shipping shape:
- JUCE plugin binary
- standalone backend helper
- optional HTML tester bundle for developer mode
- external PersonaPlex dependency or documented install path

## Catalina reality

Treat macOS Catalina as a wrapper/testing target, not an assumption that upstream PersonaPlex runs there unchanged. Verify subprocess mode and dependency installation explicitly.

## Release checklist
- plugin starts cleanly
- backend health endpoint works
- PersonaPlex link path is validated
- output folder permissions checked
- licensing and attribution text included
