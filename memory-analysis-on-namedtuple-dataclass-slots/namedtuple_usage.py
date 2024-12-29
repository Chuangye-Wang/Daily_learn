from collections import namedtuple

from memory_profiler import profile


Foobar = namedtuple("Foobar", ["x", "y"])


@profile
def main():
    f = [Foobar(42, 8) for i in range(100000)]


if __name__ == '__main__':
    main()
