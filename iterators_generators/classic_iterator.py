"""
Iterable class using the Iterator.
"""

import re
import reprlib
from collections.abc import Iterable

RE_WORD = re.compile(r'\w+')


class Sentence:
    """Sentence is iterable since it has __iter__ method.

    Use the words attribute to save matched words.
    """
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return f'Sentence({reprlib.repr(self.text)})'

    def __iter__(self):
        return SentenceIterator(self.words)


class SentenceIterator:
    """SentenceIterator is an iterator since it has __next__ and __iter__ methods."""
    def __init__(self, words):
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            # to make it iterable in for loop without error out, the StopIteration must be raised.
            raise StopIteration()
            # raise IndexError()
        self.index += 1
        return word

    def __iter__(self):
        return self


if __name__ == '__main__':
    sentence = Sentence("I will buy a car.")
    iter1 = iter(sentence)
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

