"""
Generate an arithmetic progression of numbers of any type.
Similar to range(), but this implementation can create numbers of other types (float, Decimal...)
"""

from collections.abc import Iterable


# Use class to generate arithmetic progression.
class ArithmeticProgression:
    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end  # None -> "infinite" series

    def __iter__(self):
        result_type = type(self.begin + self.step)
        result = result_type(self.begin)
        forever = self.end is None
        index = 0
        while forever or result < self.end:
            yield result
            index += 1
            result = self.begin + self.step * index


# Use generator function to generate arithmetic progression.
def aritprog_gen(begin, step, end=None):
    result = type(begin + step)(begin)
    forever = end is None
    index = 0
    while forever or result < end:
        yield result
        index += 1
        result = begin + step * index


if __name__ == "__main__":
    arith = ArithmeticProgression(1, 0.5, 2.5)
    iter1 = iter(arith)
    # iter1 is a generator.
    print("Type of iter1 is ", type(iter1))
    isinstance(iter1, Iterable)
    print(next(iter1))
    print(next(iter1))
    print(next(iter1))

    try:
        print(next(iter1))  # StopIteration raised
    except StopIteration:
        print("StopIteration raised correctly when reaching the end of the generator.")

    for i in iter(arith):
        print(i)

    iter1 = aritprog_gen(1, 0.5, 2.5)
    # iter1 is a generator.
    print("Type of iter1 is ", type(iter1))
    isinstance(iter1, Iterable)
    print(next(iter1))
    print(next(iter1))
    print(next(iter1))

    try:
        print(next(iter1))  # StopIteration raised
    except StopIteration:
        print("StopIteration raised correctly when reaching the end of the generator.")

    for i in iter(arith):
        print(i)
