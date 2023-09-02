terraform {
  cloud {
    organization = "afeld-personal"
    workspaces {
      name = "python-public-policy"
    }
  }
}

provider "google" {
  project = "fresh-mason-303504"
  region  = "us-east1"
}
