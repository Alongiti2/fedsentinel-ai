# FedSentinel-AI — Terraform Variables

variable "project_id" {
  description = "GCP Project ID"
  type        = string
  default     = "cis410-delphin"
}

variable "region" {
  description = "GCP Region"
  type        = string
  default     = "us-central1"
}

variable "environment" {
  description = "Deployment environment"
  type        = string
  default     = "dev"
  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "Environment must be dev, staging, or prod."
  }
}

variable "bigquery_dataset" {
  description = "BigQuery dataset name for threat logs"
  type        = string
  default     = "fedsentinel_threat_logs"
}

variable "alert_email" {
  description = "Email for security alerts"
  type        = string
  sensitive   = true
}
