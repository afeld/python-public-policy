# https://cloud.google.com/docs/terraform/resource-management/store-state#create_the_bucket
resource "google_storage_bucket" "backend" {
  provider      = google.backend
  name          = "python-public-policy-tf-backend"
  force_destroy = false
  location      = "us-east1"
  storage_class = "STANDARD"
  versioning {
    enabled = true
  }
}

resource "google_storage_bucket" "backend_new" {
  name          = "python-public-policy-terraform"
  force_destroy = false
  location      = data.google_client_config.current.region
  storage_class = "STANDARD"
  versioning {
    enabled = true
  }
}
