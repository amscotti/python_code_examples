from typing import Iterable

def print_triangle(n: int) -> None:
    """
    Print a Pascal's triangle with n rows.

    :param n: The number of rows in Pascal's triangle.
    """
    for row in triangle(n):
        print(" ".join(str(x) for x in row))


def triangle(n: int) -> Iterable[list[int]]:
    """
    Generate Pascal's triangle with n rows.

    :param n: The number of rows in Pascal's triangle.
    :return: A generator that yields rows of Pascal's triangle.
    """
    for row in range(n):
        temp = [1]
        for i in range(row):
            temp.append(int(temp[-1] * (row - i) / (i + 1)))
        yield temp
