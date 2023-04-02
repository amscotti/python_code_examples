def anagram(word_a: str, word_b: str) -> bool:
    """
    Check if two words are anagrams of each other.

    :param word_a: The first word to check.
    :type word_a: str
    :param word_b: The second word to check.
    :type word_b: str
    :return: True if the words are anagrams, False otherwise.
    :rtype: bool
    """
    return word_a != word_b and sorted(word_a) == sorted(word_b)


def find_anagrams(word_list: list[str]) -> dict[str, list[str]]:
    """
    Find anagrams for each word in a given list of words.

    :param word_list: A list of words for which to find anagrams.
    :type word_list: list[str]
    :return: A dictionary with each word as a key and its anagrams as a list of strings.
    :rtype: dict[str, list[str]]
    """
    output: dict[str, list[str]] = {}
    for word_a in word_list:
        output[word_a] = [word_b for word_b in word_list if anagram(word_a, word_b)]

    return output
