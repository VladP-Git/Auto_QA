def test_square_positive_numbers(math):
    """Проверка метода square для положительных чисел."""
    assert math.square(2) == 4
    assert math.square(5) == 25


def test_square_negative_numbers(math):
    """Проверка метода square для отрицательных чисел."""
    assert math.square(-3) == 9
    assert math.square(-1) == 1


def test_square_zero(math):
    """Проверка метода square для нуля."""
    assert math.square(0) == 0


def test_cube_positive_numbers(math):
    """Проверка метода cube для положительных чисел."""
    assert math.cube(3) == 27
    assert math.cube(1) == 1


def test_cube_negative_numbers(math):
    """Проверка метода cube для отрицательных чисел."""
    assert math.cube(-3) == -27
    assert math.cube(-2) == -8


def test_cube_zero(math):
    """Проверка метода cube для нуля."""
    assert math.cube(0) == 0