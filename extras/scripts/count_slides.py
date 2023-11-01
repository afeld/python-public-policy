import json
import sys


def is_slide(cell):
    SLIDE_TYPES = ["slide", "subslide"]
    slide_type = cell["metadata"].get("slideshow", {}).get("slide_type")
    return slide_type in SLIDE_TYPES


def tags(cell):
    return cell["metadata"].get("tags", [])


notebook_file = sys.argv[1]
with open(notebook_file) as f:
    notebook = json.load(f)

slides = [cell for cell in notebook["cells"] if is_slide(cell)]

columbia = [slide for slide in slides if "nyu-only" not in tags(slide)]
print("Columbia:", len(columbia))

nyu = [slide for slide in slides if "columbia-only" not in tags(slide)]
print("NYU:", len(nyu))
