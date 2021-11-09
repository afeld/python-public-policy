locals {
  local_data_dir = "/Volumes/GoogleDrive/My Drive/wagner-python/data/"

  source_files = [
    "311_community_districts.csv",
    "311_covid.csv",
    "311_mar_2019.csv",
    "311_requests_2018-19_sample.csv",
    "311_requests_2018-19_sample_clean.csv",
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
}
