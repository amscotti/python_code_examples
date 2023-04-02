LOOKUP = {
    '{': '}',
    '(': ')',
    '[': ']'
}


def balanced(input_string: str) -> bool:
    """
    Check if a string containing parentheses, brackets, and braces is balanced.

    :param input_string: The string containing parentheses, brackets, and braces.
    :type input_string: str
    :return: True if the input string is balanced, False otherwise.
    :rtype: bool
    """
    stack: list[str] = []

    for item in input_string:
        if item in LOOKUP:
            stack.append(item)
        elif item in LOOKUP.values():
            if not stack or item != LOOKUP[stack.pop()]:
                return False

    return len(stack) == 0
