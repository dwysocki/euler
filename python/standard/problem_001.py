#!/usr/bin/env python3

def main():
    print(sum(n for n in range(3, 1000)
              if n % 3 == 0 or n % 5 == 0))

if __name__ == '__main__':
    exit(main())
