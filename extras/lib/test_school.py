from .school import render_cell, SCHOOL_TEXT
from nbformat.v4 import new_markdown_cell
import pytest


@pytest.mark.parametrize("slug", [("columbia"), ("nyu")])
def test_site_path_injection(slug):
    cell = new_markdown_cell("https://python-public-policy.afeld.me/en/{{school_slug}}/README.html")
    updated_cell = render_cell(cell, slug)
    assert updated_cell.source == f"https://python-public-policy.afeld.me/en/{slug}/README.html"
