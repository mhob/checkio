#!/usr/bin/env python3

#from logzero import logger
from collections import Counter


def checkio(text: str):
    text_to_check = str()
    for character in text.lower():
        if character.isalpha():
            text_to_check += character
    counts = Counter(text_to_check)
    result = ("", 0)
    for letter in counts.keys():
        if counts[letter] > result[1]:
            result = (letter, counts[letter])
        elif letter < result[0] and counts[letter] == result[1]:
            result = (letter, counts[letter])
    return result[0]


if __name__ == "__main__":
    assert checkio("Hello World!") == "l"
    assert checkio("How do you do?") == "o"
    assert checkio("One") == "e"
    assert checkio("Oops!") == "o"
    assert checkio("AAaooo!!!!") == "a"
    assert checkio("abe") == "a"
