from .school_template import get_vars, render_template


def test_coding_env_root_url_columbia():
    vars = get_vars("columbia")
    assert vars["coding_env_url"] == vars["coding_env_root_url"]


def test_coding_env_root_url_nyu():
    vars = get_vars("nyu")
    assert vars["coding_env_root_url"].endswith(".rcnyu.org")


def test_coding_env_root_url_render():
    rendered = render_template("{{coding_env_root_url}}", "nyu")
    assert rendered.endswith(".rcnyu.org")
