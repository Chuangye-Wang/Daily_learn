from dataclasses import dataclass

from memory_profiler import profile


from memory_profiler import profile


class Foobar(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


@profile
def main():
    f = [Foobar(42, 8) for i in range(100000)]


# same memory usage as the dataclass
if __name__ == '__main__':
    main()

