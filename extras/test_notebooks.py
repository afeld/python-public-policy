import ast
from glob import glob
import os
from typing import Union
from markdown_it import MarkdownIt
from markdown_it.token import Token
import pytest
import re
from .lib.nb_helper import is_h1, is_markdown, is_python, read_notebook


def check_metadata(notebook, file, expected_kernel):
    metadata = notebook.metadata
    runtime = metadata.kernelspec.display_name

    assert runtime == expected_kernel
    assert metadata.language_info.version.startswith("3.")

    if "colab" in metadata:
        colab_name = metadata["colab"]["name"]
        assert colab_name == file, f"Name in metadata doesn't match filename for {file}."


def check_file(file, expected_kernel="Python [conda env:python-public-policy] *"):
    notebook = read_notebook(file)
    check_metadata(notebook, file, expected_kernel)


notebooks = glob("*.ipynb")
notebooks.sort()
crash_course = os.path.join(os.path.dirname(__file__), "pandas_crash_course.ipynb")
all_notebooks = notebooks + [crash_course]


@pytest.mark.parametrize("notebook", notebooks)
def test_class_notebooks(notebook):
    check_file(notebook)


def test_colab():
    # run in Google Colab
    check_file(crash_course, "Python 3")


@pytest.mark.parametrize("file", all_notebooks)
def test_one_h1(file):
    notebook = read_notebook(file)
    num_h1s = sum(is_h1(cell) for cell in notebook.cells)
    assert num_h1s == 1


@pytest.mark.parametrize("file", all_notebooks)
def test_heading_levels(file):
    notebook = read_notebook(file)
    for cell in notebook.cells:
        meta = cell.metadata
        source = cell.source
        if is_markdown(cell) and "slideshow" in meta and source.startswith("#"):
            # slide with a heading
            slide_type = meta["slideshow"]["slide_type"]
            if slide_type == "slide":
                assert source.startswith(("# ", "## ")), "should be an H1 or H2"
            elif slide_type == "subslide":
                assert source.startswith("###"), "should be H3+"


@pytest.mark.parametrize("file", notebooks)
def test_nested_lists(file):
    """JupyterBook's markdown parser doesn't support nested lists with two spaces."""

    notebook = read_notebook(file)
    for cell in notebook.cells:
        if is_markdown(cell):
            source = cell.source
            for line in source.splitlines():
                match = re.match(r"^( +)(-|\d\.)", line)
                if match:
                    num_spaces = len(match[1])
                    assert (
                        num_spaces % 3 == 0 or num_spaces % 4 == 0
                    ), f"Lists should be indented in multiples of three or four spaces. Text:\n\n{source}\n"


def check_link(token: Token, parent: Token = None):
    if token.type == "link_open":
        href = token.attrGet("href")
        # escaped Jinja2 tags
        if not re.match(r"http|#|%7B%7B", href):
            source = parent.content if parent else token.content
            assert False, f"Link should be absolute. Text:\n\n{source}\n"


@pytest.mark.parametrize("file", notebooks)
def test_links(file):
    """To ensure that links work from the coding environment, ensure all links are absolute."""

    md = MarkdownIt()

    notebook = read_notebook(file)
    for cell in notebook.cells:
        if is_markdown(cell):
            source = cell.source
            tokens = md.parse(source)
            for token in tokens:
                check_link(token)
                if token.type == "inline":
                    for child in token.children:
                        check_link(child, token)


def base_obj(node: ast.Call) -> Union[str, None]:
    """If this is a method call, return the name of the base object it was called on"""
    if isinstance(node.func, ast.Attribute) and isinstance(node.func.value, ast.Name):
        return node.func.value.id
    else:
        return None


class PlotChecker(ast.NodeVisitor):
    def visit_Call(self, node):
        if base_obj(node) == "px":
            args = [kw.arg for kw in node.keywords]
            method = node.func.attr

            if method == "get_trendline_results":
                # `title` not applicable
                return

            assert "title" in args, f"call to `{method}()` missing a `title`"


def get_tags(cell):
    return cell.metadata.get("tags", [])


@pytest.mark.parametrize("file", notebooks)
def test_chart_titles(file):
    """Make sure all charts have titles"""

    notebook = read_notebook(file)
    for cell in notebook.cells:
        tags = get_tags(cell)
        if "skip-plot-check" in tags or not is_python(cell):
            continue

        tree = ast.parse(cell.source)
        checker = PlotChecker()
        checker.visit(tree)


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


lecture_notebooks = glob("lecture_?.ipynb")
lecture_notebooks.sort()


@pytest.mark.parametrize("file", lecture_notebooks)
def test_num_slides(file):
    """Ensure there are a reasonable number of slides for each school"""

    notebook = read_notebook(file)

    # known issue that these lectures have too many slides
    if file in ["lecture_1.ipynb", "lecture_2.ipynb"]:
        return

    columbia = [cell for cell in notebook.cells if "nyu-only" not in get_tags(cell)]
    num_columbia = num_slides(columbia)
    assert num_columbia <= 62, "Too many slides for Columbia"

    nyu = [cell for cell in notebook.cells if "columbia-only" not in get_tags(cell)]
    num_nyu = num_slides(nyu)
    assert num_nyu <= 51, "Too many slides for NYU"

    # there's more Homework 0 content for Columbia, so ok to have fewer slides
    if file != "lecture_0.ipynb":
        assert (
            num_nyu <= num_columbia
        ), "NYU should have fewer slides than Columbia, since the class sessions are shorter"


hw_notebooks = glob("hw_*.ipynb")
hw_notebooks.sort()


@pytest.mark.parametrize("file", hw_notebooks)
def test_reminders(file):
    notebook = read_notebook(file)

    assert any(
        "assignments.html" in cell.source for cell in notebook.cells
    ), "Missing assignment submission instructions"

    assert any(
        "participation" in cell.source for cell in notebook.cells
    ), "Missing participation reminder"


@pytest.mark.parametrize("file", notebooks)
def test_long_outputs_scrolled(file):
    notebook = read_notebook(file)

    for cell in notebook.cells:
        if is_python(cell):
            for output in cell.outputs:
                if output.output_type == "execute_result":
                    html = output.data.get("text/html", "")
                    num_rows = html.count("<tr")
                    if num_rows > 30:
                        # if not set, the notebook will automatically scroll
                        assert (
                            cell.metadata.get("scrolled") is not False
                        ), f"Long output should be scrollable. Cell:\n\n{cell.source}\n"
