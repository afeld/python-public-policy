import json
import os
from pathlib import Path
import sys
from zipfile import ZipFile

name = sys.argv[1]
# strip off the .ipynb, if provided
name = Path(name).stem
notebook = f"{name}.ipynb"

os.makedirs("tmp", exist_ok=True)
dest = f"tmp/{name}.zip"
with ZipFile(dest, "w") as zip:
    # https://docs.codio.com/instructors/teaching/grading/nbgrader.html
    zip.writestr(".codio-jupyter", "")
    zip.write("extras/codio/.codio-menu", ".codio-menu")
    zip.write(notebook)

    # copy in the Guide config

    guide_filename = ".guides/content/Guide-bda2.json"
    with open(f"extras/codio/{guide_filename}") as f:
        guide = json.load(f)
    # specify the file that should open by default
    guide["files"][0]["path"] = notebook
    guide_json = json.dumps(guide, indent=2)
    zip.writestr(guide_filename, guide_json)

    zip.write("extras/codio/.guides/content/Guide-bda2.md", ".guides/content/Guide-bda2.md")
    zip.write("extras/codio/.guides/content/index.json", ".guides/content/index.json")

print(f"Created {dest}")
