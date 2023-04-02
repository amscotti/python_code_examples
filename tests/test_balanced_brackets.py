import pytest
from modules.balanced_brackets import balanced


@pytest.mark.parametrize("input_str,expected_result", [
    ('[]', True),
    ('()', True),
    ('{}', True),
    ('[{()}]', True),
    ('[{(something)}]', True),
    ('[{)]', False),
    ('[)(]', False),
])
def test_balanced(input_str: str, expected_result: bool):
    assert balanced(input_str) == expected_result

def load_balanced_test_cases():
    with open('tests/balanced_brackets_inputs.txt', 'r') as inputf, \
            open('tests/balanced_brackets_output.txt', 'r') as outputf:
        output = outputf.readlines()
        for index, link_input in enumerate(inputf.readlines()[1:]):
            yield link_input.strip(), output[index].strip()

@pytest.mark.parametrize("input_str,expected_result", load_balanced_test_cases())
def test_balanced_input_file(input_str: str, expected_result: bool):
    is_balanced = 'YES' if balanced(input_str) else 'NO'
    assert is_balanced == expected_result
