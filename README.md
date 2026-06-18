# 🛡️ FedSentinel-AI

> GCP-native agentic threat intelligence platform for federal environments

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://python.org)
[![GCP](https://img.shields.io/badge/Google_Cloud-Vertex_AI-orange)](https://cloud.google.com)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![FedRAMP](https://img.shields.io/badge/FedRAMP-Moderate_Aligned-blue)](docs/FEDRAMP-CONTROLS.md)

---

## Overview

**FedSentinel-AI** is an open-source proof-of-concept demonstrating how federal agencies can deploy a FedRAMP-aligned, multi-agent AI system for real-time threat detection and compliance verification using Google Cloud Platform.

Built to demonstrate enterprise-grade GCP architecture for federal cybersecurity use cases.

---

## Architecture
---

## GCP Services Used

| Service | Purpose |
|---------|---------|
| Vertex AI / Gemini | LLM inference for all 3 agents |
| Vertex AI Vector Search | RAG document retrieval |
| BigQuery | Threat log ingestion and analytics |
| Cloud Run | Serverless API deployment |
| Pub/Sub | Real-time log event streaming |
| Secret Manager | API key and credential management |
| Artifact Registry | Docker container storage |
| Workload Identity Federation | Keyless CI/CD authentication |

---

## Multi-Agent Pipeline
---

## Security & Compliance

- **FedRAMP Moderate** control alignment — see [FEDRAMP-CONTROLS.md](docs/FEDRAMP-CONTROLS.md)
- **NIST SP 800-53 Rev 5** mapped across AC, AU, SC, SI, IR, CM families
- **Zero static credentials** — Workload Identity Federation throughout
- **Snyk SAST** scanning on every pull request
- **OWASP ZAP** dynamic scanning on deployed API

---

## Project Structure
---

## Roadmap

- [x] Phase 1 — Project scaffold and architecture design
- [ ] Phase 2 — BigQuery pipeline with synthetic federal logs
- [ ] Phase 3 — RAG engine with Vertex AI Vector Search + Gemini
- [ ] Phase 4 — Multi-agent orchestration (live)
- [ ] Phase 5 — CI/CD pipeline + Cloud Run deployment
- [ ] Phase 6 — Streamlit frontend demo

---

## Author

**Delphin Zaki** | CISSP · CEH · CCSP · AWS SA Pro  
[GitHub](https://github.com/Alongiti2) · [Portfolio](https://alongiti2.github.io)
