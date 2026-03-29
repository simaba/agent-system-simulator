# Sample Output

Example run:

```text
Scenario: retry_then_success
Final outcome: Improved result accepted after retry.
Accepted: True
Retries: 1
Fallback used: False
Escalated: False
Latency (ms): 710
Estimated cost (USD): 0.019
Correctness proxy: high
Consistency note: Moderately stable but sensitive to evaluator thresholds.

Decision log:
- Planner created plan: Handle task with bounded workflow: Handle a partially ambiguous user request.
- Executor attempt 1: success=False, confidence=0.49
- Evaluator decision: accepted=False, reason=Confidence below acceptance threshold.
- Supervisor requested bounded retry.
- Executor attempt 2: success=True, confidence=0.85
- Evaluator decision: accepted=True, reason=Output meets acceptance threshold.
```
