from __future__ import annotations

from src.controller import run_scenario


def test_normal_success_path() -> None:
    report = run_scenario("normal_success")
    assert report.accepted is True
    assert report.retries == 0
    assert report.fallback_used is False
    assert report.escalated is False
    assert "Planner created plan" in report.decision_log[0]


def test_retry_then_success_path() -> None:
    report = run_scenario("retry_then_success")
    assert report.accepted is True
    assert report.retries == 1
    assert report.fallback_used is False
    assert report.escalated is False
    assert any("bounded retry" in item.lower() for item in report.decision_log)


def test_fallback_after_failure_path() -> None:
    report = run_scenario("fallback_after_failure")
    assert report.accepted is False
    assert report.fallback_used is True
    assert report.escalated is False
    assert report.final_outcome.startswith("Fallback path used")
    assert any("fallback path" in item.lower() for item in report.decision_log)
