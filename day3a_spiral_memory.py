#!/usr/bin/env python

import sys


def add(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])


def solve_spiral_route(n):
    idx = (0, 0)
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    d = 0
    i = 0
    s = 1
    t = 0
    for _ in xrange(1, n):
        idx = add(idx, dirs[d])
        i += 1
        if i == s:
            i = 0
            t += 1
            d = (d + 1) % len(dirs)
            if t == 2:
                t = 0
                s += 1

    return abs(idx[0]) + abs(idx[1])


def main():
    for line in sys.stdin:
        line = line.strip()
        if line == "":
            break
        n = int(line)
        print(solve_spiral_route(n))


if __name__ == "__main__":
    main()
