terraform {
  backend "gcs" {
    bucket = "python-public-policy-tf-backend"
    prefix = "terraform/state"
  }
}

provider "google" {
  project = "fresh-mason-303504"
  region  = "us-east1"
  alias   = "backend"
}

provider "google" {
  project = "python-public-policy2"
  region  = "us-east4"
}
