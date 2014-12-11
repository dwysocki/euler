#!/usr/bin/env python3

def digits(x):
    return map(int, str(x))

def main():
    print(sum(digits(2**1000)))

if __name__ == "__main__":
    main()
