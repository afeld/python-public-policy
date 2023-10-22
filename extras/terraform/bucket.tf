data "google_client_config" "current" {}

resource "google_storage_bucket" "data" {
  name = "python-public-policy2"
  # https://stackoverflow.com/a/64134305
  location      = data.google_client_config.current.region
  force_destroy = true

  uniform_bucket_level_access = true

  versioning {
    enabled = true
  }

  lifecycle {
    # don't give up the old bucket name before the new one is created
    create_before_destroy = true
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
