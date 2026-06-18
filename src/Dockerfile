# FedSentinel-AI — Dockerfile
# Hardened Python container for Cloud Run deployment

FROM python:3.11-slim

# Security: run as non-root user
RUN groupadd -r fedsentinel && useradd -r -g fedsentinel fedsentinel

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/

USER fedsentinel

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8080/health')"

CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8080"]
