# Instructor guide

_While this is meant as internal documentation for the instructor, others are welcome to read it._

## Adding/updating packages

1. Modify [`environment.yml`](https://github.com/afeld/python-public-policy/blob/main/extras/environment.yml)
1. Run

   ```sh
   ./extras/scripts/update_packages.sh
   ```

1. Manually update the [notebooks with interactivity](https://github.com/afeld/python-public-policy/blob/main/extras/scripts/interactive_check.sh)
1. Update environment in JupyterHub

   ```sh
   mamba env update --file extras/environment.lock.yml --prune
   ```
## Slides

While the lecture notes can be viewed as a plain notebook, they are also [visible as slides](https://nbconvert.readthedocs.io/en/latest/usage.html#reveal-js-html-slideshow).

```sh
make slides lec=N
```

## Site

The site is generated using [JupyterBook](https://jupyterbook.org/) and deployed to [ReadTheDocs](https://readthedocs.org/). Markdown (`.md`) files and the files and folders that start with an underscore (`_`) are related to JupyterBook.

The HTML can be downloaded as an [artifact](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/storing-and-sharing-data-from-a-workflow) from [the latest `Publish` Action](https://github.com/afeld/python-public-policy/actions/workflows/publish.yml).

### Building locally

1. Stage changes in Git, as they will be overwritten.
1. If on the `nyu` branch, run:

   ```sh
   ./extras/scripts/school.sh <school>
   ./extras/scripts/build.sh
   ```

1. If on `main` or other branches, run:

   ```sh
   ./extras/scripts/school_ci.sh <school>
   ```

### Checking broken links

Once the site is built, you can check broken links with:

```sh
make linkcheck
```

## Notebook cleanup

To ensure that notebooks have the correct execution order and output, run them non-interactively.

```sh
./extras/scripts/update.sh <file>.ipynb
```

## Start of class checklist

- Put out attendance sheet
- Connect to HDMI
- On laptop, turn on:
  - [Focus mode](https://support.apple.com/guide/mac-help/set-up-a-focus-to-stay-on-task-mchl613dc43f/mac)
  - [Amphetamine](https://apps.apple.com/us/app/amphetamine/id937984704?mt=12)
- Set phone to Do Not Disturb
- Run lecture notebook

- [Set placeholders](https://settings-spring.rcnyu.org/)
- Adjust lights
- If first couple classes: take attendance for recording [Academic Engagement](https://www.nyu.edu/students/student-information-and-resources/registration-records-and-graduation/albert-help/training/faculty/academic-engagement.html)
## Data sets

Canonical copies of data are in [a Google Drive folder](https://drive.google.com/drive/folders/1oCKV6NfvGO007aynTmSSbr1kzqXi4dHV), synced locally with [Google Drive for desktop](https://support.google.com/a/users/answer/9965580). Data is then compressed and uploaded to [a Google Cloud Storage bucket](https://console.cloud.google.com/storage/browser/python-public-policy/data) via [Terraform](https://github.com/afeld/python-public-policy/tree/main/extras/terraform). [Descriptions of the data sets.](https://github.com/afeld/python-public-policy/blob/main/extras/terraform/data.tf)

```sh
gcloud auth application-default login
```

## JupyterHub troubleshooting

Most of the issues are around Plotly rendering / PDF export. Things that have been hit repeatedly:

- [Embedded image error in nbconvert](https://github.com/jupyter/nbconvert/issues/2173)
  - As of 11/30/24, JupyterHub is using too new a version of pandoc in the `base` environment.
- [Plotly JupyterLab support](https://plotly.com/python/getting-started/#JupyterLab-Support)
  - [Needs to be installed on `base` environment as well](https://blog.afeld.me/getting-plotly-to-work-in-hosted-jupyterhub-26692f5ef2be)
- [PDF export fidelity](https://github.com/jupyterlab/jupyterlab/issues/12113)
- [orjson attribute error through Plotly](https://github.com/plotly/plotly.py/issues/3567)
- [PDF exporting crashes when there's a lot of data being output / in plots](../assignments.md#pdf-export)

See also: comments in [`environment.yml`](https://github.com/afeld/python-public-policy/blob/main/extras/environment.yml). Attempted to distill into the [student troubleshooting guide](../assignments.md#pdf-export).

## Contacts


- [Wagner Faculty Support](mailto:wagner.facultysupport@nyu.edu)
  - Primary contact: [Michelle Spatz](mailto:michelle.spatz@nyu.edu)
- Job posts: wagner.ocs@nyu.edu
