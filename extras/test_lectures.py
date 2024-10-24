from glob import glob
import re

import pytest

from .lib.nb_helper import get_tags, read_notebook


lecture_notebooks = glob("lecture_?.ipynb")
lecture_notebooks.sort()


def is_slide(cell):
    SLIDE_TYPES = ["slide", "subslide"]
    slide_type = cell.metadata.get("slideshow", {}).get("slide_type")
    return slide_type in SLIDE_TYPES


def num_slides(cells):
    """Return a weighted number of slides"""

    slides = [cell for cell in cells if is_slide(cell)]
    num_exercises = sum(
        1 for slide in slides if re.match("#.+exercise", slide.source, re.IGNORECASE)
    )
    # let's say that each exercise is worth ten slides
    return len(slides) + (num_exercises * 10)


@pytest.mark.parametrize("file", lecture_notebooks)
def test_num_slides(file):
    """Ensure there are a reasonable number of slides for each school"""

    notebook = read_notebook(file)

    if file in ["lecture_1.ipynb", "lecture_2.ipynb"]:
        pytest.xfail("Known issue that these lectures have too many slides")
    if file == "lecture_6.ipynb":
        pytest.xfail("The various pieces of the lecture can be scaled appropriately")

    columbia = [cell for cell in notebook.cells if "nyu-only" not in get_tags(cell)]
    num_columbia = num_slides(columbia)
    assert num_columbia <= 63, "Too many slides for Columbia"

    nyu = [cell for cell in notebook.cells if "columbia-only" not in get_tags(cell)]
    num_nyu = num_slides(nyu)
    assert num_nyu <= 51, "Too many slides for NYU"

    assert (
        num_nyu <= num_columbia
    ), "NYU should have fewer slides than Columbia, since the class sessions are shorter"
