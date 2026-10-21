from calc import Calculator

calculator = Calculator()

result = calculator.sum(2, 3)
assert result == 5
assert result != 0
assert result > 4

result = calculator.sum(-1, -3)
assert result == -4
assert result != 0
assert result < 4

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5]
result = calculator.avg(numbers)
assert result == 5

