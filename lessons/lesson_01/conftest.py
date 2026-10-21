import pytest

from calc import Calculator


@pytest.fixture
def create_calculator():
    return Calculator()