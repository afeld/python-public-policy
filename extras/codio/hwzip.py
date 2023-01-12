import os
from pathlib import Path
import sys
from zipfile import ZipFile

name = sys.argv[1]
# strip off the .ipynb, if provided
name = Path(name).stem

os.makedirs("tmp", exist_ok=True)
dest = f"tmp/{name}.zip"
with ZipFile(dest, "w") as zip:
    # https://docs.codio.com/instructors/teaching/grading/nbgrader.html
    zip.writestr(".codio-jupyter", "")
    zip.write("extras/codio/.codio-menu", ".codio-menu")
    zip.write(f"{name}.ipynb")

    zip.write("extras/codio/.guides/content/Guide-bda2.json", ".guides/content/Guide-bda2.json")
    zip.write("extras/codio/.guides/content/Guide-bda2.md", ".guides/content/Guide-bda2.md")
    zip.write("extras/codio/.guides/content/index.json", ".guides/content/index.json")

print(f"Created {dest}")
