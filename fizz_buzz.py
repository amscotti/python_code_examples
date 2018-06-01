#!/usr/bin/env python

import unittest


def fizz_buzz(stop):
    current = 1
    while current <= stop:
        if current % 15 == 0:
            yield "FizzBuzz"
        elif current % 3 == 0:
            yield "Fizz"
        elif current % 5 == 0:
            yield "Buzz"
        else:
            yield current
        current += 1


class TestFizzBuzzMethods(unittest.TestCase):
    def test_fizz_buzz_3(self):
        self.assertEqual(list(fizz_buzz(3)), [1, 2, 'Fizz'])

    def test_fizz_buzz_5(self):
        self.assertEqual(list(fizz_buzz(5)), [1, 2, 'Fizz', 4, 'Buzz'])

    def test_fizz_buzz_15(self):
        self.assertEqual(
            list(fizz_buzz(15)),
            [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz',
             'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']
        )


if __name__ == '__main__':
    unittest.main()
