from .school_template import get_vars, render_template


def test_coding_env_origin_columbia():
    vars = get_vars("columbia")
    assert vars["coding_env_url"] == vars["coding_env_origin"], "There should be no change"


def test_coding_env_origin_nyu():
    vars = get_vars("nyu")
    assert vars["coding_env_origin"].endswith(".rcnyu.org")


def test_coding_env_origin_render():
    rendered = render_template("{{coding_env_origin}}", "nyu")
    assert rendered.startswith("https://padmgp-4506")
    assert rendered.endswith(".rcnyu.org")
