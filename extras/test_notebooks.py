import os
import re
from glob import glob

import pytest
from markdown_it import MarkdownIt
from markdown_it.token import Token

from .autograder.source.tests.helpers import check_plots
from .lib.nb_helper import get_tags, is_h1, is_markdown, is_python, read_notebook


def check_metadata(notebook, file):
    metadata = notebook.metadata
    runtime = metadata.kernelspec.name

    assert runtime == "python3"
    assert metadata.language_info.version.startswith("3.")

    if "colab" in metadata:
        colab_name = metadata["colab"]["name"]
        assert colab_name == file, (
            f"Name in metadata doesn't match filename for {file}."
        )


def check_file(file):
    notebook = read_notebook(file)
    check_metadata(notebook, file)


notebooks = glob("*.ipynb")
notebooks.sort()
crash_course = os.path.join(os.path.dirname(__file__), "pandas_crash_course.ipynb")
all_notebooks = notebooks + [crash_course]


@pytest.mark.parametrize("notebook", notebooks)
def test_class_notebooks(notebook):
    check_file(notebook)


def test_colab():
    # run in Google Colab
    check_file(crash_course)


@pytest.mark.parametrize("file", all_notebooks)
def test_one_h1(file):
    notebook = read_notebook(file)
    num_h1s = sum(is_h1(cell) for cell in notebook.cells)
    assert num_h1s == 1


def get_slide_type(cell) -> str:
    return cell.metadata.get("slideshow", {}).get("slide_type", "")


def has_slides(notebook):
    return any(get_slide_type(cell) == "slide" for cell in notebook.cells)


@pytest.mark.parametrize("file", notebooks)
def test_heading_levels(file):
    notebook = read_notebook(file)

    if not has_slides(notebook):
        pytest.skip("No slides")

    for cell in notebook.cells:
        source = cell.source
        if is_markdown(cell) and source.startswith("#"):
            # it's a heading

            slide_type = get_slide_type(cell)
            if slide_type == "slide":
                assert source.startswith(("# ", "## ")), "should be an H1 or H2"
            elif slide_type == "subslide":
                assert source.startswith("###"), "should be H3+"


def check_link(token: Token, parent: Token | None = None):
    if token.type == "link_open":
        href = str(token.attrGet("href"))
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
                    for child in token.children:  # type: ignore
                        check_link(child, token)


@pytest.mark.parametrize("file", notebooks)
def test_chart_titles(file):
    """Make sure all charts have titles"""

    notebook = read_notebook(file)
    for cell in notebook.cells:
        tags = get_tags(cell)
        if "skip-plot-check" in tags or not is_python(cell):
            continue

        check_plots(cell.source)


def is_plotly_output(output):
    return "application/vnd.plotly.v1+json" in output.data


def is_text_or_table_output(output):
    return output.output_type in [
        "display_data",
        "execute_result",
    ] and not is_plotly_output(output)


def num_lines(output):
    html = output.data.get("text/html")
    if html:
        # rows of table
        return html.count("<tr")

    text = output.data["text/plain"]
    return text.count("\n")


@pytest.mark.parametrize("file", notebooks)
def test_long_outputs_scrolled(file):
    notebook = read_notebook(file)

    for cell in notebook.cells:
        if is_python(cell):
            for output in cell.outputs:
                if is_text_or_table_output(output):
                    num_rows = num_lines(output)
                    if num_rows > 30:
                        # if not set, the notebook will automatically scroll
                        assert cell.metadata.get("scrolled"), (
                            f"Long output should be scrollable. Cell:\n\n{cell.source}\n"
                        )


@pytest.mark.parametrize("file", notebooks)
def test_plotly_renderer_configured(file):
    """If a notebook imports plotly, ensure it sets the correct renderer.

    https://computing-in-context.afeld.me/notebooks.html#jupyter-book"""

    notebook = read_notebook(file)

    is_slideshow = has_slides(notebook)
    imports_plotly = False
    has_renderer_config = False

    for cell in notebook.cells:
        if is_python(cell):
            source = cell.source

            if "import plotly" in source:
                imports_plotly = True

            if 'pio.renderers.default = "notebook_connected+plotly_mimetype"' in source:
                has_renderer_config = True

                if is_slideshow:
                    assert get_slide_type(cell) == "skip", (
                        "Renderer config cell should have slide_type 'skip'"
                    )

    if imports_plotly:
        assert has_renderer_config, (
            "Notebook imports plotly but doesn't set `pio.renderers.default = 'notebook_connected+plotly_mimetype'`"
        )
