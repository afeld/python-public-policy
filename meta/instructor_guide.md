# Instructor guide

_While this is meant as internal documentation for the instructor, others are welcome to read it._

{% if id == "nyu" -%}
- JupyterHub
  - [Settings](https://settings-spring.rcnyu.org/)
  - [Instructor site](https://padmgp-4506-instructor.rcnyu.org/)
{% endif -%}

## Adding/updating packages

1. Modify [`environment.yml`](../extras/environment.yml)
1. Run

   ```sh
   ./extras/scripts/update_packages.sh
   ```

1. Manually update the [notebooks with interactivity](../extras/scripts/interactive_check.sh)
{% if id == "nyu" -%}
1. Update environment in JupyterHub

   ```sh
   mamba env update --file extras/environment.lock.yml --prune
   ```
{% endif -%}

## Slides

While the lecture notes can be viewed as a plain notebook, they are also [visible as slides](https://rise.readthedocs.io/en/stable/usage.html#running-a-slideshow).

## Site

The site is generated using [JupyterBook](https://jupyterbook.org/) and deployed to [ReadTheDocs](https://readthedocs.org/). Markdown (`.md`) files and the files and folders that start with an underscore (`_`) are related to JupyterBook.

1. If not on the `{{school_slug}}` branch, render the files. _**This will overwrite local files, and thus you should stage changes first.**_

      ```sh
      ./extras/scripts/school.sh <school>
      ```

1. Build the site.

      ```sh
      ./extras/scripts/build.sh
      ```

You can then check broken links with

```sh
ruby ./extras/scripts/broken_links.rb
```

## Notebook cleanup

To ensure that notebooks have the correct execution order and output, run them non-interactively.

```sh
./extras/scripts/update.sh <file>.ipynb
```

## Start of class checklist

- Zoom
  1. Start meeting
  1. From {% if id == "columbia" %}Zoom Classroom{% else %}the podium PC{% endif %}, `Join Meeting`
  1. If there's a guest, [make them a co-host](https://support.zoom.us/hc/en-us/articles/206330935-Enabling-and-Adding-a-Co-Host#h_9c3ee7f2-b70c-4061-8dcf-00dd836b2075)
  {% if id == "nyu" -%}
  1. Ensure all the cameras are turned on
  {% endif -%}
  1. On laptop, mute mic and speakers
  {% if id == "columbia" -%}
  1. Turn on the wireless mic
  1. From the control panel, open Settings and ensure the wireless mic is unmuted
  {% else -%}
  1. On Zoom Classroom, unmute mic
  {% endif -%}
  1. Confirm audio being received in Zoom
  1. Share screen
  1. Start recording
{% if id == "nyu" -%}
- [Set placeholders](https://settings-spring.rcnyu.org/)
- If first couple classes: take attendance for recording [Academic Engagement](https://www.nyu.edu/students/student-information-and-resources/registration-records-and-graduation/albert-help/training/faculty/academic-engagement.html)
{% endif -%}

## Data sets

Canonical copies of data are in [a Google Drive folder](https://drive.google.com/drive/folders/1oCKV6NfvGO007aynTmSSbr1kzqXi4dHV), synced locally with [Google Drive for desktop](https://support.google.com/a/users/answer/9965580). Data is then compressed and uploaded to [a Google Cloud Storage bucket](https://console.cloud.google.com/storage/browser/python-public-policy/data) via [Terraform](../extras/terraform/). [Descriptions of the data sets.](../extras/terraform/data.tf)

{% if id == "columbia" -%}
## Student enrollment activity

1. Visit [SSOL](https://ssol.columbia.edu)
1. View the Wait List Activity
1. Open the Console
1. Paste [the script](../extras/scripts/ssol.js)
1. Do the same for the other section(s)
{% endif %}
