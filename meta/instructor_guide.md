# Instructor guide

_While this is meant as internal documentation for the instructor, others are welcome to read it._

## Adding/updating packages

1. Modify [`requirements.txt`](https://github.com/afeld/python-public-policy/blob/main/requirements.txt)
1. Run

   ```sh
   make update_packages
   ```

1. Manually update the [notebooks with interactivity](https://github.com/afeld/python-public-policy/blob/main/extras/scripts/interactive_check.sh)

## Slides

While the lecture notes can be viewed as a plain notebook, they are also [visible as slides](https://nbconvert.readthedocs.io/en/latest/usage.html#reveal-js-html-slideshow).

```sh
make slides lec=N
```

## Site

The site is generated using [JupyterBook](https://jupyterbook.org/) and deployed to [ReadTheDocs](https://readthedocs.org/). Markdown (`.md`) files and the files and folders that start with an underscore (`_`) are related to JupyterBook.

### Publishing

This repository produces separate versions of the course site for Columbia and NYU. The source of truth is the `main` branch; the `columbia` and `nyu` branches contain generated, school-specific source files and their rendered sites.

For each school, [the workflow](../.github/actions/setup/action.yml):

1. Checks out the repository and installs the Python dependencies.
1. Switches to the corresponding school branch and merges the pushed branch using Git's `ours` strategy. It then restores the pushed branch's working tree. This records that the school branch includes the source revision without using the school branch's generated files as merge inputs.
1. Commits that preliminary source tree.
1. Runs [`school_ci.sh`](../extras/scripts/school_ci.sh) with the school ID. The script removes files that do not belong in a published school version, including development tools and tests.
1. Calls [`school.sh`](../extras/scripts/school.sh) to render school-specific templates.
   - Jinja templating is used throughout the source files (Markdown, notebooks, etc.), rendered using [nbconvert](https://nbconvert.readthedocs.io/) with [a custom preprocessor](../extras/lib/school_template.py).
   - Variables (such as `{{school_name}}`, `{{lms_url}}`, and `{{assistant_name}}`) are replaced with the values from the [configuration file](../extras/lib/school.py) for the selected school.
   - It uses {% raw %}`{% if id == "columbia" %}` and `{% if id == "nyu" %}`{% endraw %} conditionals for school-only content; the generated files must contain neither Jinja tags nor identifiers for the other school.
   - For notebooks, `school.sh` first removes cells tagged for the other school (`columbia-only` or `nyu-only`) and cells tagged `remove`. It then renders each remaining cell source with the same Jinja variables, while resetting notebook kernel metadata to the default Python kernel for Colab.
1. Runs `make site`, which builds the Jupyter Book HTML into `_build/html`.
1. When the push is to `main`, the workflow pushes the amended commit to the relevant school branch. Pushes to other branches still render both versions and upload their HTML, but do not update either published branch.
1. ReadTheDocs is notified of updates to the school-specific branches, which are then built as separate [versions](https://docs.readthedocs.com/platform/stable/versions.html).

The HTML can be downloaded as an [artifact](https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/storing-and-sharing-data-from-a-workflow) from [the latest `Publish` Action](https://github.com/afeld/python-public-policy/actions/workflows/publish.yml).

### Building locally

1. Stage changes in Git, as they will be overwritten.
1. If on the `{{school_slug}}` branch, run:

   ```sh
   make site
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
- Connect to screen
- Start [Amphetamine](https://apps.apple.com/us/app/amphetamine/id937984704?mt=12)
- Set phone and laptop to Do Not Disturb
- Run lecture notebook
{% if id == "columbia" -%}
- Put out power strips
{% endif -%}

## Data sets

Canonical copies of data are in [a Google Drive folder](https://drive.google.com/drive/folders/1oCKV6NfvGO007aynTmSSbr1kzqXi4dHV), synced locally with [Google Drive for desktop](https://support.google.com/a/users/answer/9965580). Data is then compressed and uploaded to [a Google Cloud Storage bucket](https://console.cloud.google.com/storage/browser/python-public-policy/data) via [Terraform](https://github.com/afeld/python-public-policy/tree/main/extras/terraform). [Descriptions of the data sets.](https://github.com/afeld/python-public-policy/blob/main/extras/terraform/data.tf)

```sh
gcloud auth application-default login
```

{% if id == "columbia" -%}
## Student enrollment activity

This only shows students coming off the wait list.

1. Visit [SSOL](https://ssol.columbia.edu)
1. View the Wait List Activity
1. Open the Console
1. Paste [the script](https://github.com/afeld/python-public-policy/blob/main/extras/scripts/ssol.js)
1. Do the same for the other section(s)

## End of course

1. Open [{{lms_name}}]({{lms_url}})
1. Go to Grades
1. Update the curve
   1. Export -> Export Entire Gradebook
   1. In the [curve notebook](../curve.ipynb), update the CSV filename
   1. Re-run the notebook
   1. Spot-check the [new cutoffs](../curve.ipynb#new-cutoffs)
   1. Update the [course grading scheme](https://community.canvaslms.com/t5/Instructor-Guide/How-do-I-enable-a-grading-scheme-for-a-course/ta-p/1042)
1. [Calculate the attendance scores](../extras/scripts/attendance.py)
1. Confirm all Gradebook cells are filled in
{% else -%}
## Autograder

Requires [Docker](https://www.docker.com/). Put files in `extras/autograder/submission/`, then run:

```sh
make autograde
```
{%- endif %}

## Contacts

{% if id == "columbia" -%}
- [SIPA Academic Affairs](mailto:sipa_academicaffairs@sipa.columbia.edu)
  - Primary contact: [Jenny Labuga-Rumenik](mailto:jl5701@columbia.edu)
- Job posts: sipajobs@sipa.columbia.edu
{%- else %}
- [Wagner Faculty Support](mailto:wagner.facultysupport@nyu.edu)
  - Primary contact: [Michelle Spatz](mailto:michelle.spatz@nyu.edu)
- Job posts: wagner.ocs@nyu.edu
{%- endif %}
