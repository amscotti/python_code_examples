def first_unique_letter(word: str) -> str | None:
    """
    Return the first unique letter in a given string.

    :param word: The input string to search for unique letters.
    :type word: str
    :return: The first unique letter found in the input string, or None if no unique letter is found.
    :rtype: str or None
    """
    return next((char for char in word if word.count(char) == 1), None)
