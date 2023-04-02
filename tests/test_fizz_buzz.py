import pytest
from modules.fizz_buzz import fizz_buzz


@pytest.mark.parametrize("n,expected_result", [
    (0, []),
    (1, [1]),
    (2, [1, 2]),
    (3, [1, 2, 'Fizz']),
    (4, [1, 2, 'Fizz', 4]),
    (5, [1, 2, 'Fizz', 4, 'Buzz']),
    (15, [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']),
])
def test_fizz_buzz(n: int, expected_result: list):
    assert list(fizz_buzz(n)) == expected_result