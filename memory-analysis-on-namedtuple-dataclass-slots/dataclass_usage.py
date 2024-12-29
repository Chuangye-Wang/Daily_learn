from dataclasses import dataclass

from memory_profiler import profile


@dataclass
class Foobar:
    x: int
    y: int

@profile
def main():
    f = [Foobar(42, 8) for i in range(100000)]


if __name__ == '__main__':
    main()
