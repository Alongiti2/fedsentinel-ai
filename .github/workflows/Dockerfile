# FedSentinel-AI — Dockerfile
# Hardened Python container for Cloud Run deployment

FROM python:3.11-slim

# Security: run as non-root user
RUN groupadd -r fedsentinel && useradd -r -g fedsentinel fedsentinel

# Set working directory
WORKDIR /app

# Install dependencies first (layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY src/ ./src/

# Security: switch to non-root user
USER fedsentinel

# Expose port
EXPOSE 8080

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8080/health')"

# Start FastAPI server
CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8080"]
