import pytest
from .autograder.source.tests.helpers import check_plots


def test_check_plots_good():
    check_plots('px.line(df, x="year", y="life_expectancy", title="Life expectancy")')


def test_check_plots_get_trendline_results():
    check_plots("px.get_trendline_results(fig)")


def test_check_plots_no_plotly():
    check_plots("")


def test_check_plots_no_title():
    with pytest.raises(AssertionError):
        check_plots('px.line(df, x="year", y="life_expectancy")')
