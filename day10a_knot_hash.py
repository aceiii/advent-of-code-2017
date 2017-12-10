#!/usr/bin/env python

import sys


def twist(knot, current, span):
    n = len(knot)
    for i in xrange(span / 2):
        a_pos = (current + i) % n
        b_pos = (current + span - 1 - i) % n
        a = knot[a_pos]
        b = knot[b_pos]
        knot[a_pos] = b
        knot[b_pos] = a


def solve_knot_hash(N, spans):
    knot = range(N)
    current = 0
    skip = 0
    for span in spans:
        twist(knot, current, span)
        current += span + skip
        skip += 1

    return knot[0] * knot[1]


def main():
    N = 256
    for line in sys.stdin:
        spans = map(int, line.split(","))
        print(solve_knot_hash(N, spans))


if __name__ == "__main__":
    main()
