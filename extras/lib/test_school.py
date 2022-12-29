from .school import render_cell
from nbformat.v4 import new_markdown_cell


def test_site_path_injection():
    cell = new_markdown_cell("https://python-public-policy.afeld.me/en/{{school_slug}}/README.html")
    updated_cell = render_cell(cell, "someschool")
    assert updated_cell.source == "https://python-public-policy.afeld.me/en/someschool/README.html"
