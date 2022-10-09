#!/usr/bin/env python

import unittest

LOOKUP = {
    '{': '}',
    '(': ')',
    '[': ']'
}


def balanced(input_string: str) -> str:
    stack: list[str] = []

    for item in input_string:
        if item in LOOKUP:
            stack.append(item)
        elif item in LOOKUP.values():
            if not stack:
                return 'NO'
            if item != LOOKUP[stack.pop()]:
                return 'NO'

    return 'YES' if not stack else 'NO'


class TestBalancedMethods(unittest.TestCase):
    def test_balanced_true(self):
        self.assertEqual(balanced('[{()}]'), 'YES')

    def test_balanced_false(self):
        self.assertEqual(balanced('[{)]'), 'NO')

    def test_balanced_input_file(self):
        with open('balanced_brackets_inputs.txt', 'r') as inputf, \
                open('balanced_brackets_output.txt', 'r') as outputf:
            output = outputf.readlines()
            for index, link_input in enumerate(inputf.readlines()[1:]):
                self.assertEqual(balanced(link_input.strip()),
                                 output[index].strip())


if __name__ == '__main__':
    unittest.main()
