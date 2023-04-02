import pytest
from modules.pascal_triangle import triangle, print_triangle
from io import StringIO
from contextlib import redirect_stdout


@pytest.mark.parametrize("level,expected_result", [
    (1, [[1]]),
    (2, [[1], [1, 1]]),
    (3, [[1], [1, 1], [1, 2, 1]]),
    (4, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]),
    (5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]),
    (6, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]])
])
def test_triangle(level: int, expected_result: list[list[int]]):
    assert list(triangle(level)) == expected_result


@pytest.mark.parametrize("level,expected_output", [
    (1, "1\n"),
    (2, "1\n1 1\n"),
    (3, "1\n1 1\n1 2 1\n"),
    (4, "1\n1 1\n1 2 1\n1 3 3 1\n"),
])
def test_print_triangle(level: int, expected_output: str):
    with redirect_stdout(StringIO()) as output:
        print_triangle(level)
    assert output.getvalue() == expected_output
