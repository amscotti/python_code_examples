import pytest
from modules.anagram import anagram, find_anagrams


@pytest.mark.parametrize("word_a,word_b,expected_result", [
    ("bad", "tad", False),
    ("cat", "tas", False),
    ("bad", "dab", True),
    ("listen", "silent", True),
    ("triangle", "integral", True),
    ("apple", "pleap", True),
])
def test_anagram(word_a: str, word_b: str, expected_result: bool):
    assert anagram(word_a, word_b) == expected_result


@pytest.mark.parametrize("word_list,expected_result", [
    (["bad", "dab", "adb", "hot", "toh", "ggg"], {
        'dab': ['bad', 'adb'],
        'bad': ['dab', 'adb'],
        'hot': ['toh'],
        'ggg': [],
        'adb': ['bad', 'dab'],
        'toh': ['hot']
    }),
    (["listen", "silent", "apple", "leppa", "triangle", "integral", "cat"], {
        'listen': ['silent'],
        'silent': ['listen'],
        'apple': ['leppa'],
        'leppa': ['apple'],
        'triangle': ['integral'],
        'integral': ['triangle'],
        'cat': []
    }),
    (["abc", "def", "ghi"], {
        'abc': [],
        'def': [],
        'ghi': []
    }),
    ([], {}),
])
def test_find_anagrams(word_list: list[str], expected_result: dict[str, list[str]]):
    assert find_anagrams(word_list) == expected_result
