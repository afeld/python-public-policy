import pytest
from .school import EXEMPT


@pytest.mark.parametrize("phrase", EXEMPT)
def test_exempt(phrase):
    assert phrase == phrase.lower(), f"{phrase} should be lowercase"
