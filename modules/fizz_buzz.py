from typing import Generator, Union

def fizz_buzz(stop: int) -> Generator[Union[str, int], None, None]:
    """
    Generate the FizzBuzz sequence up to a given stop value.

    :param stop: The maximum value to generate in the sequence.
    :type stop: int
    :return: A generator object that yields strings of "Fizz", "Buzz", "FizzBuzz", or integers.
    :rtype: Generator[Union[str, int], None, None]
    """
    for current in range(1, stop+1):
        if current % 15 == 0:
            yield "FizzBuzz"
        elif current % 3 == 0:
            yield "Fizz"
        elif current % 5 == 0:
            yield "Buzz"
        else:
            yield current
        current += 1
