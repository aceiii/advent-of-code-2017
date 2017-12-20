#!/usr/bin/env python

import sys


def solve_circular_spinlock(n, steps):
    a = [0]
    p = 0
    for i in xrange(1, n + 1):
        p = ((p + steps) % len(a)) + 1
        a.insert(p, i)

    return a[(p + 1) % len(a)]


def main():
    N = 2017
    for line in sys.stdin:
        line = line.strip()
        if line == "":
            break
        print(solve_circular_spinlock(N, int(line)))


if __name__ == "__main__":
    main()
