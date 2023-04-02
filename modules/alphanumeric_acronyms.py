def alphanumeric_acronyms(word: str, prefix: int = 1) -> str:
    """
    Generate an alphanumeric acronym for a given word.

    :param word: The input word for which to generate the acronym.
    :type word: str
    :param prefix: The number of characters to keep at the beginning of the word (default is 1).
    :type prefix: int
    :return: The alphanumeric acronym for the input word.
    :rtype: str
    """
    if len(word) > prefix + 2:
        return f"{word[:prefix]}{len(word[prefix:-1])}{word[-1]}"
    else:
        return word


def alphanumeric_acronyms_list(word_list: list[str], prefix: int = 1) -> list[str]:
    """
    Generate a list of unique alphanumeric acronyms for a list of words.

    :param word_list: The input list of words for which to generate acronyms.
    :type word_list: list[str]
    :param prefix: The number of characters to keep at the beginning of each word (default is 1).
    :type prefix: int
    :return: A list of unique alphanumeric acronyms for the input words.
    :rtype: list[str]
    """
    output: dict[str, list[str]] = {}
    for word in word_list:
        acronym = alphanumeric_acronyms(word, prefix)
        output.setdefault(acronym, []).append(word)

    clean = [key for key, value in output.items() if len(value) == 1]
    colliding = [value for key, value in output.items() if len(value) > 1]

    if colliding:
        flat_colliding = [item for sublist in colliding for item in sublist]
        clean.extend(alphanumeric_acronyms_list(flat_colliding, prefix + 1))

    return clean
