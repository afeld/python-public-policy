import json
import os
from pathlib import Path
import sys
from zipfile import ZipFile


def read_json(filename):
    with open(filename) as f:
        return json.load(f)


name = sys.argv[1]
# strip off the .ipynb, if provided
name = Path(name).stem
notebook_filename = f"{name}.ipynb"

os.makedirs("tmp", exist_ok=True)
dest = f"tmp/{name}.zip"
with ZipFile(dest, "w") as zip:
    # https://docs.codio.com/instructors/teaching/grading/nbgrader.html
    zip.writestr(".codio-jupyter", "")
    zip.write("extras/codio/.codio-menu", ".codio-menu")

    # modify the kernel, since we aren't using a conda environment
    notebook = read_json(notebook_filename)
    notebook["metadata"]["kernelspec"] = (
        {"display_name": "Python 3", "language": "python", "name": "python3"},
    )
    notebook_json = json.dumps(notebook, indent=2)
    zip.writestr(notebook_filename, notebook_json)

    # copy in the Guide config

    guide_filename = ".guides/content/Guide-bda2.json"
    guide = read_json(f"extras/codio/{guide_filename}")
    # specify the file that should open by default
    guide["files"][0]["path"] = notebook_filename
    guide_json = json.dumps(guide, indent=2)
    zip.writestr(guide_filename, guide_json)

    zip.write("extras/codio/.guides/content/Guide-bda2.md", ".guides/content/Guide-bda2.md")
    zip.write("extras/codio/.guides/content/index.json", ".guides/content/index.json")

print(f"Created {dest}")
