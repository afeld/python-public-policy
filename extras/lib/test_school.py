from nbformat.v4 import new_markdown_cell
import pytest

from .school import SCHOOL_TEXT
from .school_template import confirm_other_schools_not_included, render_cell


@pytest.mark.parametrize("id", [("columbia"), ("nyu")])
def test_site_path_injection(id):
    school = SCHOOL_TEXT[id]
    cell = new_markdown_cell("https://python-public-policy.afeld.me/en/{{school_slug}}/")

    updated_cell = render_cell(cell, id)

    expected = f"https://python-public-policy.afeld.me/en/{school.school_slug}/"
    assert updated_cell.source == expected


def test_other_school():
    confirm_other_schools_not_included("Something something Columbia", "columbia")
    with pytest.raises(AssertionError):
        confirm_other_schools_not_included("Something something NYU", "columbia")
