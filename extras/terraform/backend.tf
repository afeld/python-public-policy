# https://cloud.google.com/docs/terraform/resource-management/store-state#create_the_bucket
resource "google_storage_bucket" "backend" {
  name          = "python-public-policy-terraform"
  force_destroy = false
  location      = data.google_client_config.current.region
  storage_class = "STANDARD"
  versioning {
    enabled = true
  }
}

moved {
  from = google_storage_bucket.backend_new
  to   = google_storage_bucket.backend
}
