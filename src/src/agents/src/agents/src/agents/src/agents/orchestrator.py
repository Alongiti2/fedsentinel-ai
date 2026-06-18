# FedSentinel-AI — Orchestrator Agent
# Master agent that coordinates Agent 1, 2, and 3 into a unified pipeline

from .threat_classifier import ThreatClassifierAgent
from .compliance_checker import ComplianceCheckerAgent
from .remediation_advisor import RemediationAdvisorAgent

class OrchestratorAgent:
    """
    Master Orchestrator — FedSentinel-AI
    
    Coordinates the full multi-agent pipeline:
    Step 1: ThreatClassifierAgent  → classify the log event
    Step 2: ComplianceCheckerAgent → check NIST/FedRAMP compliance
    Step 3: RemediationAdvisorAgent → generate remediation plan
    Step 4: Assemble and return unified threat report
    
    This is the single entry point called by the FastAPI endpoint.
    """

    def __init__(self):
        self.threat_classifier = ThreatClassifierAgent()
        self.compliance_checker = ComplianceCheckerAgent()
        self.remediation_advisor = RemediationAdvisorAgent()

    def run(self, log_event: dict) -> dict:
        """
        Full pipeline execution.
        Input:  raw federal log event
        Output: complete threat intelligence report
        """
        print(f"[Orchestrator] Processing log event: {log_event.get('event_type', 'UNKNOWN')}")

        # Step 1 — Classify threat
        threat = self.threat_classifier.classify(log_event)
        print(f"[Orchestrator] Threat classified: {threat['severity']}")

        # Step 2 — Check compliance
        compliance = self.compliance_checker.check(log_event, threat)
        print(f"[Orchestrator] Compliance checked: violation={compliance['violation_detected']}")

        # Step 3 — Generate remediation
        remediation = self.remediation_advisor.advise(threat, compliance)
        print(f"[Orchestrator] Remediation plan generated")

        # Step 4 — Assemble final report
        return {
            "status": "complete",
            "log_event": log_event,
            "threat_analysis": threat,
            "compliance_report": compliance,
            "remediation_plan": remediation
        }
