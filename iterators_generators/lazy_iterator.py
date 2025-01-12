"""
Iterable class using generator.
- No need to have a words list.
- No need to create a SentenceIterator class.
"""

import re
import reprlib
from collections.abc import Iterable

RE_WORD = re.compile(r"\w+")


class Sentence:
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return f"Sentence({reprlib.repr(self.text)})"

    def __iter__(self):
        for match in RE_WORD.finditer(self.text):
            yield match.group()


if __name__ == "__main__":
    sentence = Sentence("I will buy a car.")
    iter1 = iter(sentence)
    # iter1 is a generator.
    print("Type of iter1 is ", type(iter1))
    isinstance(iter1, Iterable)

    print(next(iter1))
    print(next(iter1))
    print(next(iter1))
    print(next(iter1))
    print(next(iter1))

    try:
        print(next(iter1))  # StopIteration raised
    except StopIteration:
        print("StopIteration raised correctly when reaching the end of the generator.")

    for word in iter(sentence):
        print(word)
