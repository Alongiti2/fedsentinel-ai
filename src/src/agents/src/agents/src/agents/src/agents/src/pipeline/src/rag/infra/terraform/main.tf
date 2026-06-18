# FedSentinel-AI — Terraform Infrastructure
# GCP-native federal threat intelligence platform

terraform {
  required_version = ">= 1.5.0"
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
  backend "gcs" {
    bucket = "fedsentinel-ai-tfstate"
    prefix = "terraform/state"
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
}

# --- Artifact Registry ---
resource "google_artifact_registry_repository" "fedsentinel" {
  location      = var.region
  repository_id = "fedsentinel-ai"
  format        = "DOCKER"
  description   = "FedSentinel-AI container images"
}

# --- Cloud Run Service ---
resource "google_cloud_run_v2_service" "fedsentinel_api" {
  name     = "fedsentinel-api"
  location = var.region

  template {
    containers {
      image = "${var.region}-docker.pkg.dev/${var.project_id}/fedsentinel-ai/api:latest"
      resources {
        limits = {
          cpu    = "2"
          memory = "1Gi"
        }
      }
    }
    service_account = google_service_account.fedsentinel_sa.email
  }
}

# --- Service Account ---
resource "google_service_account" "fedsentinel_sa" {
  account_id   = "fedsentinel-deploy-sa"
  display_name = "FedSentinel AI Deploy Service Account"
}

# --- Secret Manager (API Keys) ---
resource "google_secret_manager_secret" "gemini_api_key" {
  secret_id = "gemini-api-key"
  replication {
    auto {}
  }
}
