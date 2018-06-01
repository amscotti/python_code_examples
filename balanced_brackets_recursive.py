#!/usr/bin/env python

import sys
import unittest

sys.setrecursionlimit(2000)

LOOKUP = {
    "{": "}",
    "(": ")",
    "[": "]"
}


def balanced(input_string, stack):
    if not input_string and not stack:
        return "YES"
    elif not input_string and stack:
        return "NO"
    elif input_string[0] in LOOKUP:
        return balanced(input_string[1:], ([input_string[0]] + stack))
    elif stack and LOOKUP[stack[0]] == input_string[0]:
        return balanced(input_string[1:], stack[1:])
    return "NO"


class TestBalancedMethods(unittest.TestCase):
    def test_balanced_true(self):
        self.assertEqual(balanced("[{()}]", []), "YES")

    def test_balanced_false(self):
        self.assertEqual(balanced("[{)]", []), "NO")

    def test_balanced_input_file(self):
        with open("balanced_brackets_inputs.txt", "r") as inputf, \
                open("balanced_brackets_output.txt", "r") as outputf:
            output = outputf.readlines()
            for index, link_input in enumerate(inputf.readlines()[1:]):
                self.assertEqual(balanced(link_input.strip(), []),
                                 output[index].strip())


if __name__ == '__main__':
    unittest.main()
