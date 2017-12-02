#!/usr/bin/env python
# pylint: disable=all

import sys


def solve_captcha(arr):
    total = 0

    n = len(arr)
    for i in xrange(n):
        a = arr[i]
        b = arr[(i + (n/2)) % n]
        total += a if a == b else 0

    return total


def main():
    for line in sys.stdin:
        print solve_captcha(map(int, list(line.strip())))


if __name__ == "__main__":
    main()
