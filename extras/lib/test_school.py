from .school import render_cell, confirm_other_schools_not_included, SCHOOL_TEXT
from nbformat.v4 import new_markdown_cell
import pytest


@pytest.mark.parametrize("slug", [("columbia"), ("nyu")])
def test_site_path_injection(slug):
    cell = new_markdown_cell("https://python-public-policy.afeld.me/en/{{school_slug}}/README.html")
    updated_cell = render_cell(cell, slug)
    assert updated_cell.source == f"https://python-public-policy.afeld.me/en/{slug}/README.html"


def test_other_school_columbia():
    school = SCHOOL_TEXT["columbia"]

    confirm_other_schools_not_included("Something something Columbia", school.school_slug)
    with pytest.raises(AssertionError):
        confirm_other_schools_not_included("Something something NYU", school.school_slug)


def test_other_school_nyu():
    school = SCHOOL_TEXT["nyu"]

    confirm_other_schools_not_included("Something something NYU", school.school_slug)
    with pytest.raises(AssertionError):
        confirm_other_schools_not_included("Something something Columbia", school.school_slug)
