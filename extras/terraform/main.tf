terraform {
  required_version = "1.1.7"
}

provider "google" {
  project = "fresh-mason-303504"
  region  = "us-east1"
}

resource "google_storage_bucket" "data" {
  name          = "python-public-policy"
  location      = "US-EAST1"
  force_destroy = true

  versioning {
    enabled = true
  }
}

locals {
  data_dir = "data"
}

# make publicly readable
resource "google_storage_bucket_access_control" "public_rule" {
  bucket = google_storage_bucket.data.name
  role   = "READER"
  entity = "allUsers"
}

data "google_project" "project" {
}

output "bucket_console" {
  value = "https://console.cloud.google.com/storage/browser/${google_storage_bucket.data.name}/${local.data_dir}?authuser=1&project=${data.google_project.project.project_id}"
}
