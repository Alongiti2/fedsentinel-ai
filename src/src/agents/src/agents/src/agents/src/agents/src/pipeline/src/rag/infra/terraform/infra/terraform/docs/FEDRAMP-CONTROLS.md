# FedSentinel-AI — FedRAMP/NIST Security Controls Mapping

This document maps the FedSentinel-AI architecture to NIST SP 800-53 Rev 5
security controls, demonstrating alignment with FedRAMP Moderate baseline.

---

## Access Control (AC)

| Control | Title | FedSentinel-AI Implementation |
|---------|-------|-------------------------------|
| AC-2 | Account Management | GCP IAM with least-privilege service accounts |
| AC-3 | Access Enforcement | Workload Identity Federation — no static keys |
| AC-6 | Least Privilege | Dedicated SA per service with scoped roles |
| AC-17 | Remote Access | Cloud Run private ingress, VPC Service Controls |

---

## Audit and Accountability (AU)

| Control | Title | FedSentinel-AI Implementation |
|---------|-------|-------------------------------|
| AU-2 | Event Logging | GCP Cloud Audit Logs enabled on all services |
| AU-3 | Content of Audit Records | BigQuery stores full log payload + metadata |
| AU-9 | Protection of Audit Info | BigQuery table IAM — write-once audit logs |
| AU-12 | Audit Record Generation | Pub/Sub pipeline captures all log events |

---

## System and Communications Protection (SC)

| Control | Title | FedSentinel-AI Implementation |
|---------|-------|-------------------------------|
| SC-8 | Transmission Confidentiality | TLS 1.3 enforced on all Cloud Run endpoints |
| SC-12 | Cryptographic Key Management | Secret Manager with CMEK encryption |
| SC-28 | Protection at Rest | GCP default encryption + Secret Manager |

---

## System and Information Integrity (SI)

| Control | Title | FedSentinel-AI Implementation |
|---------|-------|-------------------------------|
| SI-3 | Malicious Code Protection | Snyk SAST scanning in CI/CD pipeline |
| SI-4 | System Monitoring | Real-time threat detection via Gemini agents |
| SI-10 | Information Input Validation | FastAPI input validation on all endpoints |

---

## Incident Response (IR)

| Control | Title | FedSentinel-AI Implementation |
|---------|-------|-------------------------------|
| IR-4 | Incident Handling | Automated remediation plans via Agent 3 |
| IR-5 | Incident Monitoring | BigQuery dashboard + Looker Studio alerts |
| IR-6 | Incident Reporting | Structured JSON reports with severity levels |

---

## Configuration Management (CM)

| Control | Title | FedSentinel-AI Implementation |
|---------|-------|-------------------------------|
| CM-2 | Baseline Configuration | Terraform IaC — all infra version controlled |
| CM-3 | Configuration Change Control | GitHub Actions PR-gated deployments |
| CM-8 | System Component Inventory | Artifact Registry tracks all container images |

---

*Mapped to NIST SP 800-53 Rev 5 and FedRAMP Moderate Baseline.*
*Last updated: June 2026*
