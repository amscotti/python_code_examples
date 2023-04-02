import pytest
from modules.alphanumeric_acronyms import alphanumeric_acronyms, alphanumeric_acronyms_list

@pytest.mark.parametrize("word,expected_result", [
    ("internationalization", "i18n"),
    ("localization", "l10n"),
    ("electromagnetic", "e13c"),
    ("pneumonoultramicroscopicsilicovolcanoconiosis", "p43s"),
])
def test_alphanumeric_acronyms(word: str, expected_result: str):
    assert alphanumeric_acronyms(word) == expected_result

@pytest.mark.parametrize("word_list,expected_result", [
    (["internationalization", "localization"], ['i18n', 'l10n']),
    (["localization", "internationalization"], ['l10n', 'i18n']),
    ([
        "hydrochemistry",
        "historiography",
        "histochemistry",
        "ferromagnetic",
        "ferroelectric",
        "hallucinogenic",
        "hermaphroditic"
    ], [
        "hy11y",
        "ha11c",
        "he11c",
        "histoc7y",
        "histor7y",
        "ferrom6c",
        "ferroe6c"
    ])
])
def test_alphanumeric_acronyms_list(word_list: list[str], expected_result: list[str]):
    assert sorted(alphanumeric_acronyms_list(word_list)) == sorted(expected_result)

def test_alphanumeric_acronyms_unchanged():
    word = "localization"
    assert alphanumeric_acronyms(word, len(word)) == "localization"