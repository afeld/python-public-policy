# Contributing

- JupyterHub
  - [Settings](https://settings-fall.rcnyu.org/)
  - [Instructor site](https://padmgp-4506001-fall-instructor.rcnyu.org/)

## Adding/updating packages

1. Modify [`environment.yml`](../extras/environment.yml)
1. Run

   ```sh
   ./extras/scripts/update_packages.sh
   ```

1. Manually update the [notebooks with interactivity](../extras/scripts/interactive_check.sh)
1. Update other environment(s) (e.g. JupyterHub)

   ```sh
   mamba env update --file environment.yml --prune
   ```

## Slides

While the lecture notes can be viewed as a plain notebook, they are also [visible as slides](https://rise.readthedocs.io/en/stable/usage.html#running-a-slideshow).

## Site

The site is generated using [JupyterBook](https://jupyterbook.org/) and deployed to [ReadTheDocs](https://readthedocs.org/). The files and folders that start with an underscore (`_`) are related to JupyterBook. Build locally from the `columbia` or `nyu` branches with:

```sh
jupyter-book build .
```

## Notebook cleanup

To ensure that notebooks have the correct execution order and output, run them non-interactively.

```sh
./extras/scripts/update.sh <file>.ipynb
```

## Start of class checklist

- Zoom
  1. Start meeting
  1. From Zoom Classroom, `Join Meeting`
  1. Ensure all the cameras are turned on
  1. Mute mic and speakers on computer
  1. Unmute mic on Zoom Classroom
  1. Start recording
- [Set placeholders](https://settings-fall.rcnyu.org/)
- If first couple classes: take attendance for recording [Academic Engagement](https://www.nyu.edu/students/student-information-and-resources/registration-records-and-graduation/albert-help/training/faculty/academic-engagement.html)

## Data sets

Canonical copies of data are in [a Google Drive folder](https://drive.google.com/drive/folders/1oCKV6NfvGO007aynTmSSbr1kzqXi4dHV), synced locally with [Google Drive for desktop](https://support.google.com/a/users/answer/9965580). Data is then compressed and uploaded to [a Google Cloud Storage bucket](https://console.cloud.google.com/storage/browser/python-public-policy/data) via [Terraform](../extras/terraform/). [Descriptions of the data sets.](../extras/terraform/data.tf)
