#!/usr/bin/env python

import unittest


def print_triangle(n):
    for row in triangle(n):
        print(" ".join(str(x) for x in row))


def triangle(n):
    for row in range(n):
        temp = [1]
        for i in range(row):
            temp.append(int(temp[-1] * (row - i) * 1 / (i + 1)))
        yield temp


class TestTriangleMethods(unittest.TestCase):
    def test_triangle_level_1(self):
        self.assertEqual(list(triangle(1)), [[1]])

    def test_triangle_level_2(self):
        self.assertEqual(list(triangle(2)), [
            [1],
            [1, 1]
        ])

    def test_triangle_level_3(self):
        self.assertEqual(list(triangle(3)), [
            [1],
            [1, 1],
            [1, 2, 1]
        ])

    def test_triangle_level_4(self):
        self.assertEqual(list(triangle(4)), [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1]
        ])

    def test_triangle_level_5(self):
        self.assertEqual(list(triangle(5)), [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1]
        ])

    def test_triangle_level_6(self):
        self.assertEqual(list(triangle(6)), [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1],
            [1, 5, 10, 10, 5, 1]
        ])


if __name__ == '__main__':
    unittest.main()
