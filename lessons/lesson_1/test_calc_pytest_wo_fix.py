from calc import Calculator
import pytest

def test_sum_positive_numbers():
    calculator = Calculator()
    assert calculator.sum(2, 4) == 6
    assert calculator.sum(2, 5) == 7
    assert calculator.sum(1, 8) == 9

def test_sum_negative_numbers():
    calculator = Calculator()
    assert calculator.sum(-2, -4) == -6
    assert calculator.sum(-2, -5) == -7
    assert calculator.sum(-1, -8) == -9


