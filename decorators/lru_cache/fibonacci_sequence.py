import functools
import sys
import time


"""
Use lru_cache when:
- Function is deterministic and pure
- You want better performance
- Input space is limited or has frequent repetitions

Avoid it when:
- Inputs are unique every time
- Memory usage is critical
- Function has side effects
"""


def time_checker(func):
    """Decorator to measure the execution time of a function."""

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        print(f"Result = {result}")
        print(f"Execution time: {end_time - start_time:.4f} seconds")
        print(f"Function '{func.__name__}' executed with arguments: {args}, {kwargs}")
        return result

    return wrapper


@functools.lru_cache(maxsize=1500)
def fibonacci_cache(n: int) -> int:
    """Calculate the nth Fibonacci number using memoization.

    Even with cache, python could raise RecursionError
    - maximum recursion depth exceeded in comparison due to the default recursion limit in python.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    elif n < 2:
        return n
    else:
        return fibonacci_cache(n - 1) + fibonacci_cache(n - 2)


def fibonacci_no_cache(n: int) -> int:
    """Calculate the nth Fibonacci number without memoization."""
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    elif n < 2:
        return n
    else:
        return fibonacci_no_cache(n - 1) + fibonacci_no_cache(n - 2)


def fibonacci_dp(n: int) -> int:
    """Calculate the nth Fibonacci number using dynamic programming."""
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    elif n < 2:
        return n
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b

        return b


def test_fibonacci_cache():
    sys.setrecursionlimit(1500)
    time_checker(func=fibonacci_cache)(500)


def test_fibonacci_no_cache():
    # very slow due to many repetitive calculations
    sys.setrecursionlimit(1500)
    time_checker(func=fibonacci_no_cache)(20)


def test_fibonacci_dp():
    time_checker(func=fibonacci_dp)(500)
