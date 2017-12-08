#!/usr/bin/env python

import sys


def add(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])


def neighbour_sum(m, idx):
    dirs = [(1, 0), (1, 1), (0, 1),
            (-1, 1), (-1, 0), (-1, -1),
            (0, -1), (1, -1)]
    t = 0
    for d in dirs:
        try:
            t += m[add(idx, d)]
        except Exception:
            pass
    return t


def solve_spiral_sum_greater_than(n):
    m = {(0, 0): 1}
    idx = (0, 0)
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    d = 0
    i = 0
    s = 1
    t = 0
    while m[idx] <= n:
        idx = add(idx, dirs[d])
        m[idx] = neighbour_sum(m, idx)
        i += 1
        if i == s:
            i = 0
            t += 1
            d = (d + 1) % len(dirs)
            if t == 2:
                t = 0
                s += 1

    return m[idx]


def main():
    for line in sys.stdin:
        line = line.strip()
        if line == "":
            break
        n = int(line)
        print(solve_spiral_sum_greater_than(n))


if __name__ == "__main__":
    main()
