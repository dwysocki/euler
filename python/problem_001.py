#!/usr/bin/env python3
"""Problem 1
Finds the sum of all multiples of 3 or 5 between 0 and 1000.
"""

import numpy

def main():
    numbers = numpy.arange(3, 1000)
    selection = numpy.logical_or((numbers % 3) == 0,
                                 (numbers % 5) == 0)
    print(numbers[selection].sum())

if __name__ == '__main__':
    exit(main())
