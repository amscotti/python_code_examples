#!/usr/bin/env python

import unittest


def alphanumeric_acronyms(word: str, prefix=1) -> str:
    if len(word) > prefix + 2:
        return "{}{}{}".format(word[0:prefix], len(word[prefix:-1]), word[-1])
    else:
        return word


def alphanumeric_acronyms_list(word_list: list[str], prefix=1) -> list[str]:
    output: dict[str, list[str]] = {}
    for word in word_list:
        acronyms = alphanumeric_acronyms(word, prefix)
        output.setdefault(acronyms, []).append(word)

    clean = [key for (key, value) in output.items() if len(value) == 1]
    collusion = [value for (key, value) in output.items() if len(value) > 1]

    if collusion:
        clean.extend(
            alphanumeric_acronyms_list(
                [item for sublist in collusion for item in sublist],
                prefix + 1
            )
        )

    return clean


class TestAlphanumericAcronymsMethods(unittest.TestCase):
    def test_alphanumeric_acronyms_internationalization(self):
        self.assertEqual(alphanumeric_acronyms("internationalization"), "i18n")

    def test_alphanumeric_acronyms_localization(self):
        self.assertEqual(alphanumeric_acronyms("localization"), "l10n")

    def test_alphanumeric_acronyms_list_words(self):
        self.assertEqual(alphanumeric_acronyms_list(
            ["internationalization", "localization"]),
            ['i18n', 'l10n'])

    def test_alphanumeric_acronyms_list_collusion_words(self):
        self.assertEqual(sorted(alphanumeric_acronyms_list([
            'hydrochemistry',
            'historiography',
            'histochemistry',
            'ferromagnetic',
            'ferroelectric',
            'hallucinogenic',
            'hermaphroditic'])),
            sorted([
                'hy11y',
                'ha11c',
                'he11c',
                'histoc7y',
                'histor7y',
                'ferrom6c',
                'ferroe6c']))


if __name__ == '__main__':
    unittest.main()
