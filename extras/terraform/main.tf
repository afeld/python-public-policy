terraform {
  backend "gcs" {
    bucket = "python-public-policy-terraform"
    prefix = "state"
  }
}

# match the region that the NYU JupyterHub is in

provider "google" {
  project = "fresh-mason-303504"
  region  = "us-east1"
  alias   = "backend"
}

provider "google" {
  project = "python-public-policy2"
  region  = "us-east1"
}
