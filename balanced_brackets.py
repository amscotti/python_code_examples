#!/usr/bin/env python

import unittest

CLOSING_LOOKUP = {
    "{": "}",
    "(": ")",
    "[": "]"
}


def balanced(input_string):
    stack = []
    input_length = len(input_string)
    if input_length == 0 or input_length % 2 != 0 or not input_string[0] in CLOSING_LOOKUP:
        return "NO"

    stack.insert(0, input_string[0])

    for index in range(1, input_length):
        if input_string[index] in CLOSING_LOOKUP:
            stack.insert(0, input_string[index])
        elif not stack and not input_string[index] in CLOSING_LOOKUP:
            break
        elif CLOSING_LOOKUP[stack[0]] == input_string[index]:
            stack.pop(0)
        else:
            break

    if not stack and index == (input_length - 1):
        return "YES"
    else:
        return "NO"


class TestBalancedMethods(unittest.TestCase):

    def test_balanced_true(self):
        self.assertEqual(balanced("[{()}]"), "YES")

    def test_balanced_false(self):
        self.assertEqual(balanced("[{)]"), "NO")

    def test_balanced_input_file(self):
        with open("balanced_brackets_inputs.txt", "r") as file_input:
            with open("balanced_brackets_output.txt", "r") as file_output:
                output = file_output.readlines()
                for index, link_input in enumerate(file_input.readlines()[1:]):
                    self.assertEqual(balanced(link_input.strip()), output[index].strip())

if __name__ == '__main__':
    unittest.main()
