import pytest
from simple_math import SimpleMath


@pytest.fixture
def math():
    """Фикстура для создания экземпляра класса SimpleMath перед тестами."""
    return SimpleMath()