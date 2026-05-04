# Changelog

All notable changes to this project will be documented in this file.

## [0.1.0] — Foundation release

### Added

- Runnable multi-agent simulator demonstrating bounded orchestration behavior.
- Scenario runs for normal success, retry-then-success, and fallback-after-failure.
- Tests for controller and workflow behavior.
- CI workflow that installs the package, runs pytest, and executes documented scenarios across supported Python versions.
- Sample output artifact for explaining simulator behavior.
- Documentation explaining how the simulator connects to `multi-agent-governance`, `agent-orchestration`, and `agent-eval`.

### Notes

This repository is the executable proof point for the multi-agent governance cluster. It intentionally avoids real LLM calls and enterprise observability so the control logic remains small, inspectable, and safe to study.

### Next

- Add JSON output for scenario runs.
- Map simulator output into the `agent-eval` report schema.
- Add adversarial and prompt-injection inspired scenarios.
- Add more failure-mode coverage for tool unavailability and escalation misses.
