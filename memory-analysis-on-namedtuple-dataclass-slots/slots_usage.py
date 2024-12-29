from memory_profiler import profile


class Foobar(object):
    __slots__ = ("x", "y")
    def __init__(self, x, y):
        self.x = x
        self.y = y


@profile
def main():
    f = [Foobar(42, 8) for i in range(100000)]


if __name__ == '__main__':
    main()
