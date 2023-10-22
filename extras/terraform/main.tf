terraform {
  backend "gcs" {
    bucket = "python-public-policy-terraform"
    prefix = "state"
  }
}

provider "google" {
  project = "python-public-policy2"
  # match the region that the NYU JupyterHub is in
  region = "us-east1"
}
