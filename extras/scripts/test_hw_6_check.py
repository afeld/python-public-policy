import nbformat
from .hw_6_check import has_plotting, includes_link


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


def test_includes_link_base():
    cells = []
    assert not includes_link(cells)


def test_includes_link_missing():
    cells = [nbformat.from_dict({"cell_type": "markdown", "source": ""})]
    assert not includes_link(cells)


def test_includes_link_markdown():
    cells = [nbformat.from_dict({"cell_type": "markdown", "source": "https://google.com"})]

    assert includes_link(cells)


def test_includes_link_code_only():
    cells = [nbformat.from_dict({"cell_type": "code", "source": "https://google.com"})]
    assert not includes_link(cells)


def test_includes_link_code_comment():
    cells = [nbformat.from_dict({"cell_type": "code", "source": "# https://google.com"})]
    assert includes_link(cells)
