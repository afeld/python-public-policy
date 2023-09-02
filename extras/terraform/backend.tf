# https://cloud.google.com/docs/terraform/resource-management/store-state#create_the_bucket
resource "google_storage_bucket" "backend" {
  name          = "python-public-policy-tf-backend"
  force_destroy = false
  location      = "us-east1"
  storage_class = "STANDARD"
  versioning {
    enabled = true
  }
}
