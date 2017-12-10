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


def dense_hash_xor(elems):
    a = 0
    for b in elems:
        a ^= b
    return a


def solve_knot_hash(N, spans):
    knot = range(N)
    current = 0
    skip = 0
    rounds = 64
    for _ in xrange(rounds):
        for span in spans:
            twist(knot, current, span)
            current += span + skip
            skip += 1

    size = 16
    i = 0
    xored = []
    while i < N:
        a = knot[i:i+size]
        x = dense_hash_xor(a)
        xored.append(x)
        i += size

    return "".join(map(lambda x: hex(x)[2:], xored))


def main():
    N = 256
    for line in sys.stdin:
        spans = map(ord, line.strip()) + [17, 31, 73, 47, 23]
        print(solve_knot_hash(N, spans))


if __name__ == "__main__":
    main()
