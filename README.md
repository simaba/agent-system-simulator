# Agent System Simulator

A small runnable simulator for controlled multi-agent workflows.

## Why this repository exists

This repository turns governance, orchestration, and evaluation concepts into a working reference implementation.

It demonstrates a small agent system with:
- explicit roles,
- bounded retries,
- fallback behavior,
- escalation triggers,
- structured logs,
- and a lightweight evaluation summary.

## Included agents

- **Planner**: decides how the task should be handled
- **Executor**: performs the main task action
- **Evaluator**: checks whether the result is acceptable
- **Supervisor**: decides whether to accept, retry, fallback, or escalate

## Example scenarios

- `normal_success`
- `retry_then_success`
- `fallback_after_failure`

## Quick start

```bash
python run_demo.py --scenario normal_success
```

## What the simulator outputs

Each run produces:
- a decision log,
- retry and escalation events,
- final outcome,
- latency,
- cost estimate,
- and a small evaluation summary.

## Repository structure

- `run_demo.py`
- `src/agents.py`
- `src/controller.py`
- `src/evaluation.py`
- `src/scenarios.py`
- `examples/sample-output.md`

## Design principle

A multi-agent system should not only produce outputs. It should also expose control logic clearly enough to be debugged, evaluated, and improved.
