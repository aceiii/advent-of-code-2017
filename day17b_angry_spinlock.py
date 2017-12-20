#!/usr/bin/env python

import sys


def solve_circular_spinlock(n, steps):
    p = 0
    vals = {}
    for i in xrange(1, n + 1):
        p = ((p + steps) % i) + 1
        vals[p] = i
    return vals[1]


def main():
    N = 50000000
    for line in sys.stdin:
        line = line.strip()
        if line == "":
            break
        print(solve_circular_spinlock(N, int(line)))


if __name__ == "__main__":
    main()
