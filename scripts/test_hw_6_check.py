from .hw_6_check import has_plotting


def test_nothing():
    assert not has_plotting("")


def test_plotly():
    assert has_plotting("import plotly.express as px")
