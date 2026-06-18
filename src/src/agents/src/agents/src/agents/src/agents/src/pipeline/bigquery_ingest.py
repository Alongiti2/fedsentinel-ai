# FedSentinel-AI — BigQuery Ingestion Pipeline
# Streams federal log events into BigQuery for analysis

from datetime import datetime
import json

# BigQuery table schema for federal threat logs
SCHEMA = {
    "table": "federal_threat_logs",
    "fields": [
        {"name": "timestamp",   "type": "TIMESTAMP"},
        {"name": "source_ip",   "type": "STRING"},
        {"name": "event_type",  "type": "STRING"},
        {"name": "severity",    "type": "STRING"},
        {"name": "agency_id",   "type": "STRING"},
        {"name": "user_id",     "type": "STRING"},
        {"name": "resource",    "type": "STRING"},
        {"name": "raw_payload", "type": "JSON"},
    ]
}

class BigQueryIngestor:
    """
    Streams federal SIEM log events into BigQuery.
    
    Data flow:
    SIEM Source → Pub/Sub → Cloud Function → BigQuery
    
    TODO Phase 2: Wire up real Pub/Sub trigger
    """

    def __init__(self, project_id: str, dataset: str):
        self.project_id = project_id
        self.dataset = dataset
        # TODO Phase 2: Initialize google-cloud-bigquery client
        self.client = None

    def ingest(self, log_event: dict) -> dict:
        """
        Normalizes and inserts a log event into BigQuery.
        """
        row = {
            "timestamp": datetime.utcnow().isoformat(),
            "source_ip": log_event.get("source_ip", "0.0.0.0"),
            "event_type": log_event.get("event_type", "UNKNOWN"),
            "severity": log_event.get("severity", "LOW"),
            "agency_id": log_event.get("agency_id", "UNKNOWN"),
            "user_id": log_event.get("user_id", "UNKNOWN"),
            "resource": log_event.get("resource", "UNKNOWN"),
            "raw_payload": json.dumps(log_event)
        }
        # TODO Phase 2: self.client.insert_rows_json(table, [row])
        print(f"[BigQuery] Row ready for insertion: {row['event_type']}")
        return row

def generate_synthetic_log() -> dict:
    """
    Generates a synthetic federal SIEM log event for testing.
    Mimics real Splunk/SIEM output format.
    """
    return {
        "timestamp": datetime.utcnow().isoformat(),
        "source_ip": "192.168.10.45",
        "event_type": "UNAUTHORIZED_ACCESS_ATTEMPT",
        "severity": "HIGH",
        "agency_id": "DOD-AGENCY-001",
        "user_id": "user_7743",
        "resource": "/api/classified/documents",
        "raw_payload": {"method": "GET", "status": 403}
    }
