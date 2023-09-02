terraform {
  backend "gcs" {
    bucket = "python-public-policy-tf-backend"
    prefix = "terraform/state"
  }
}

provider "google" {
  project = "fresh-mason-303504"
  region  = "us-east1"
}
