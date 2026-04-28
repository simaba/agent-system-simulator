# How This Simulator Connects to the Agent Governance Portfolio

`agent-simulator` is the runnable proof point for the multi-agent governance cluster.

It does not replace the surrounding framework repositories. It makes their ideas concrete.

## Repository roles

| Repository | Role | How this simulator relates |
|---|---|---|
| [`multi-agent-governance`](https://github.com/simaba/multi-agent-governance) | defines ownership, trust boundaries, oversight, and escalation | this simulator demonstrates bounded escalation and traceable control decisions |
| [`agent-orchestration`](https://github.com/simaba/agent-orchestration) | catalogs control-flow patterns such as retry, fallback, validation, and escalation | this simulator implements a small controlled workflow with retry, fallback, and supervisor decisions |
| [`agent-eval`](https://github.com/simaba/agent-eval) | defines evaluation dimensions, scorecards, and release evidence | this simulator emits acceptance, retry, fallback, escalation, latency, cost, and correctness-proxy signals |
| [`agent-simulator`](https://github.com/simaba/agent-simulator) | provides executable examples | this repo is intentionally small so the control logic stays readable |

## What this simulator demonstrates

- explicit agent roles: planner, executor, evaluator, supervisor
- bounded retry rather than unbounded loops
- fallback after repeated failure
- escalation flagging
- decision logs that can be reviewed later
- lightweight quality and operational metrics

## What it intentionally does not demonstrate

- real LLM calls
- production observability
- broad benchmark coverage
- enterprise-grade tool orchestration
- automated governance approval workflows

Those are deliberately out of scope so the repo remains small, inspectable, and safe for learning and testing.

## Suggested use in the portfolio

Use this repo when a reader asks:

> What does accountable multi-agent control logic look like in code?

Then point to:

1. `multi-agent-governance` for the governance model
2. `agent-orchestration` for pattern options
3. `agent-eval` for measurement and release evidence
4. `agent-simulator` for the executable demonstration
