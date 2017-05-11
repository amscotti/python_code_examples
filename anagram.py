#!/usr/bin/env python

import unittest


def anagram(word_a, word_b):
    return word_a != word_b and sorted(word_a) == sorted(word_b)


def find_anagrams(word_list):
    output = {}
    for word_a in word_list:
        output.setdefault(word_a, []).extend([word_b for word_b in word_list if anagram(word_a, word_b)])
    return output


class TestFindAnagramsMethods(unittest.TestCase):

    def test_anagram_true(self):
        self.assertTrue(anagram("bad", "dab"))

    def test_anagram_false(self):
        self.assertFalse(anagram("bad", "tad"))

    def test_find_anagrams(self):
        self.assertEqual(find_anagrams(["bad", "dab", "adb", "hot", "toh", "ggg"]),
                         {'dab': ['bad', 'adb'],
                          'bad': ['dab', 'adb'],
                          'hot': ['toh'],
                          'ggg': [],
                          'adb': ['bad', 'dab'],
                          'toh': ['hot']})


if __name__ == '__main__':
    unittest.main()
