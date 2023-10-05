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
resource "google_storage_bucket_iam_binding" "public" {
  bucket = google_storage_bucket.data.name
  role   = "roles/storage.objectViewer"
  members = [
    "allUsers",
  ]
}

data "google_project" "project" {
}

output "bucket_console" {
  value = "https://console.cloud.google.com/storage/browser/${google_storage_bucket.data.name}/${local.data_dir}?authuser=1&project=${data.google_project.project.project_id}"
}
