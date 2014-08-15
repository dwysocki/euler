#!/usr/bin/env python3
"""Problem 1
Finds the sum of all multiples of 3 or 5 between 0 and 1000.
"""

def main():
    print(sum(n for n in range(3, 1000)
              if n % 3 == 0 or n % 5 == 0))

if __name__ == '__main__':
    exit(main())
