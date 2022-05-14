from .hw_6_check import has_plotting


def test_nothing():
    assert not has_plotting("")


def test_seaborn():
    assert has_plotting("import seaborn as sns")


def test_plotly():
    assert has_plotting("import plotly.express as px")


def test_plot_method():
    assert has_plotting("df.plot()")


def test_plot_submodule():
    assert has_plotting("df.plot.scatter()")
