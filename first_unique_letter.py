#!/usr/bin/env python

import unittest


def first_unique_letter(word):
    return next((i for i in word if word.count(i) == 1), None)


class TestFirstUniqueLetterMethods(unittest.TestCase):
    def test_first_unique_letter_a(self):
        self.assertEqual(first_unique_letter('abc'), 'a')

    def test_first_unique_letter_b(self):
        self.assertEqual(first_unique_letter('aabc'), 'b')

    def test_first_unique_letter_c(self):
        self.assertEqual(first_unique_letter('aabbc'), 'c')

    def test_first_unique_letter_none(self):
        self.assertEqual(first_unique_letter('aabbcc'), None)


if __name__ == '__main__':
    unittest.main()
