# Security Policy — FedSentinel-AI

## Reporting a Vulnerability

If you discover a security vulnerability, please do NOT open a public issue.
Email: delphinzaki@gmail.com

We will respond within 48 hours and provide a fix timeline.

## Security Measures

- All secrets managed via GCP Secret Manager
- Zero static credentials — Workload Identity Federation only
- Snyk SAST scanning on every pull request
- OWASP ZAP dynamic scanning on deployed API
- Non-root Docker container execution
- TLS 1.3 enforced on all endpoints

## Supported Versions

| Version | Supported |
|---------|-----------|
| 0.1.x   | ✅ Yes    |

## Compliance

See [FEDRAMP-CONTROLS.md](docs/FEDRAMP-CONTROLS.md) for full
NIST SP 800-53 / FedRAMP Moderate control mapping.
