import pytest
from nbformat.v4 import new_code_cell, new_markdown_cell

from .school import SCHOOL_TEXT
from .school_template import (
    REPO_ROOT,
    confirm_other_schools_not_included,
    render_cell,
)


@pytest.mark.parametrize("id", [("columbia"), ("nyu")])
def test_site_path_injection(id):
    school = SCHOOL_TEXT[id]
    cell = new_markdown_cell(
        "https://python-public-policy.afeld.me/en/{{school_slug}}/"
    )

    updated_cell = render_cell(cell, id)

    expected = f"https://python-public-policy.afeld.me/en/{school.school_slug}/"
    assert updated_cell.source == expected


def test_other_school():
    confirm_other_schools_not_included("Something something Columbia", "columbia")
    with pytest.raises(AssertionError):
        confirm_other_schools_not_included("Something something NYU", "columbia")


@pytest.mark.parametrize(
    "target,expected",
    [
        ("syllabus.md", "syllabus/"),
        ("syllabus.md#academic-integrity", "syllabus/#academic-integrity"),
        (
            "assignments/open_ended.md#storing-data",
            "assignments/open-ended/#storing-data",
        ),
        ("lecture_1_exercise.ipynb", "lecture-1-exercise/"),
        ("index.md", ""),
        ("index.md#why-this-class", "#why-this-class"),
    ],
)
def test_relative_link(target: str, expected: str):
    cell = new_markdown_cell(f"See [this]({target}).")

    updated_cell = render_cell(cell, "columbia")

    url = f"https://python-public-policy.afeld.me/en/columbia/{expected}"
    assert updated_cell.source == f"See [this]({url})."


def test_relative_link_from_subdirectory():
    cell = new_markdown_cell("[Syllabus](../syllabus.md)")

    updated_cell = render_cell(cell, "nyu", REPO_ROOT / "final_project")

    assert (
        updated_cell.source
        == "[Syllabus](https://python-public-policy.afeld.me/en/nyu/syllabus/)"
    )


@pytest.mark.parametrize(
    "source",
    [
        "[Colab](https://colab.research.google.com/notebooks/io.ipynb)",
        "[Below](#some-heading)",
        "![project flow](extras/img/projectflow.png)",
        "[email](mailto:someone@example.com)",
    ],
)
def test_other_links_unchanged(source: str):
    cell = new_markdown_cell(source)

    updated_cell = render_cell(cell, "columbia")

    assert updated_cell.source == source


def test_code_cell_links_unchanged():
    cell = new_code_cell("# [Syllabus](syllabus.md)")

    updated_cell = render_cell(cell, "columbia")

    assert updated_cell.source == "# [Syllabus](syllabus.md)"


def test_missing_link_target():
    cell = new_markdown_cell("[Gone](not_a_page.md)")

    with pytest.raises(AssertionError, match="not_a_page.md"):
        render_cell(cell, "columbia")
