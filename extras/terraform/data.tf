locals {
  local_data_dir = "/Users/afeld/Library/CloudStorage/GoogleDrive-alf9@nyu.edu/My Drive/wagner-python/data"

  # find all with
  #
  #   grep -oh -E "https://storage.googleapis.com/python-public-policy/data/.+\.csv(\.zip)?" *.ipynb | xargs basename | sort | uniq
  source_files = [
    "311_community_districts.csv",
    # replaced by
    "community_district_311.csv",

    "311_covid.csv",
    "311_mar_2019.csv",

    # sample of `311_Service_Requests_2018-19.csv`, using following method with `n=500000` and `random_state=1`
    # https://gist.github.com/afeld/a7a62271923c7a079d02f8f38efc0a78
    "311_requests_2018-19_sample.csv",

    # `311_requests_2018-19_sample.csv` with junk filtered out. See lecture 1.
    "311_requests_2018-19_sample_clean.csv",

    # Original data from
    # https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9
    # Leaving out because it slows the terraform operations down too much.
    # "311_Service_Requests_2018-19.csv",

    "cleaned_311_data_hw2.csv"
  ]
}

data "archive_file" "zipped" {
  for_each = toset(local.source_files)

  type        = "zip"
  source_file = "${local.local_data_dir}/${each.key}"
  output_path = "${local.local_data_dir}/${each.key}.zip"
}

resource "google_storage_bucket_object" "zipped" {
  for_each = data.archive_file.zipped

  name   = "data/${basename(each.value.output_path)}"
  source = each.value.output_path
  bucket = google_storage_bucket.data.name

  timeouts {
    create = "20m"
    update = "20m"
  }
}

# test that the files are publicly accessible
data "http" "publicly_accessible" {
  for_each = google_storage_bucket_object.zipped

  url    = "https://storage.googleapis.com/${google_storage_bucket.data.name}/${each.value.name}"
  method = "HEAD"

  lifecycle {
    postcondition {
      condition     = self.status_code == 200
      error_message = "Status code invalid"
    }
  }
}
