import pytest
from modules.first_unique_letter import first_unique_letter


@pytest.mark.parametrize("input_str,expected_result", [
    ('abc', 'a'),
    ('aabc', 'b'),
    ('aabbc', 'c'),
    ('aabbcc', None),
    ('', None),
    ('abcdef', 'a'),
    ('aaabbbccc', None),
    ('aaabbbcccd', 'd'),
    ('aabccbddc', None)
])
def test_first_unique_letter(input_str: str, expected_result: str):
    assert first_unique_letter(input_str) == expected_result