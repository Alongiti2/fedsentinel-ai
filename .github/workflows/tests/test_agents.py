# FedSentinel-AI — Unit Tests
# Tests for all 3 agents and the orchestrator pipeline

import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.agents.threat_classifier import ThreatClassifierAgent
from src.agents.compliance_checker import ComplianceCheckerAgent
from src.agents.remediation_advisor import RemediationAdvisorAgent
from src.agents.orchestrator import OrchestratorAgent
from src.pipeline.bigquery_ingest import generate_synthetic_log

# --- Sample test log event ---
SAMPLE_LOG = {
    "timestamp": "2026-06-18T10:00:00Z",
    "source_ip": "192.168.10.45",
    "event_type": "UNAUTHORIZED_ACCESS_ATTEMPT",
    "severity": "HIGH",
    "agency_id": "DOD-AGENCY-001",
    "user_id": "user_7743",
    "resource": "/api/classified/documents"
}

class TestThreatClassifierAgent:
    def test_classify_returns_dict(self):
        agent = ThreatClassifierAgent()
        result = agent.classify(SAMPLE_LOG)
        assert isinstance(result, dict)

    def test_classify_has_required_keys(self):
        agent = ThreatClassifierAgent()
        result = agent.classify(SAMPLE_LOG)
        assert "agent" in result
        assert "threat_type" in result
        assert "severity" in result
        assert "confidence" in result

class TestComplianceCheckerAgent:
    def test_check_returns_dict(self):
        agent = ComplianceCheckerAgent()
        threat = {"severity": "HIGH"}
        result = agent.check(SAMPLE_LOG, threat)
        assert isinstance(result, dict)

    def test_check_has_required_keys(self):
        agent = ComplianceCheckerAgent()
        threat = {"severity": "HIGH"}
        result = agent.check(SAMPLE_LOG, threat)
        assert "agent" in result
        assert "violation_detected" in result
        assert "nist_reference" in result

class TestRemediationAdvisorAgent:
    def test_advise_returns_dict(self):
        agent = RemediationAdvisorAgent()
        result = agent.advise({"severity": "HIGH"}, {"violation_detected": True})
        assert isinstance(result, dict)

    def test_advise_has_required_keys(self):
        agent = RemediationAdvisorAgent()
        result = agent.advise({"severity": "HIGH"}, {"violation_detected": True})
        assert "agent" in result
        assert "priority" in result
        assert "immediate_actions" in result

class TestOrchestratorAgent:
    def test_run_returns_complete_report(self):
        orchestrator = OrchestratorAgent()
        result = orchestrator.run(SAMPLE_LOG)
        assert isinstance(result, dict)
        assert "threat_analysis" in result
        assert "compliance_report" in result
        assert "remediation_plan" in result
        assert result["status"] == "complete"

class TestSyntheticLogGenerator:
    def test_generates_valid_log(self):
        log = generate_synthetic_log()
        assert isinstance(log, dict)
        assert "event_type" in log
        assert "severity" in log
        assert "agency_id" in log
