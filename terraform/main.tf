provider "google" {
  project = "python-public-policy"
  region  = "us-central1"
}

resource "google_storage_bucket" "data" {
  name     = "python-public-policy"
  location = "US-CENTRAL1"

  versioning {
    enabled = true
  }
}

# make publicly readable
resource "google_storage_bucket_access_control" "public_rule" {
  bucket = google_storage_bucket.data.name
  role   = "READER"
  entity = "allUsers"
}
