#!/usr/bin/env python3
"""Problem 2
Finds the sum of all even numbers in the Fibonacci sequence under 4 million
"""

from itertools import takewhile

def fibonacci():
    pprev = 1
    prev = 2

    yield pprev
    yield prev

    while True:
        current = pprev + prev
        pprev = prev
        prev = current
        yield current

def evenp(n):
    return n % 2 == 0

def main():
    print(sum(filter(evenp, takewhile(lambda i: i < 4000000, fibonacci()))))


if __name__ == '__main__':
    exit(main())
