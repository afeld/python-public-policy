from urllib.parse import parse_qs, urlparse

from nbformat.v4 import new_markdown_cell
import pytest

from .school import SCHOOL_TEXT
from .school_template import (
    confirm_other_schools_not_included,
    render_cell,
    get_vars,
    render_template,
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


def test_render_template():
    rendered = render_template("{{coding_env_url}}", "nyu")

    assert "&amp;" not in rendered, "Query separators shouldn't be encoded"

    url = urlparse(rendered)
    query = parse_qs(url.query)
    assert query == {
        "repo": ["https://github.com/afeld/python-public-policy"],
        "urlpath": ["tree/python-public-policy/"],
        "branch": ["nyu"],
    }, "Should contain the nbgitpuller URL"


def test_coding_env_origin_columbia():
    vars = get_vars("columbia")
    assert vars["coding_env_url"] == vars["coding_env_origin"], (
        "There should be no change"
    )


def test_coding_env_origin_nyu():
    vars = get_vars("nyu")
    assert vars["coding_env_origin"].endswith(".rcnyu.org")


def test_coding_env_origin_render():
    rendered = render_template("{{coding_env_origin}}", "nyu")
    assert rendered.startswith("https://padmgp-4506")
    assert rendered.endswith(".rcnyu.org")
