#!/usr/bin/env python

import sys
from string import rjust


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


def knot_hash(spans):
    N = 256
    knot = range(N)
    current = 0
    skip = 0
    rounds = 64
    hash_spans = map(ord, spans.strip()) + [17, 31, 73, 47, 23]
    for _ in xrange(rounds):
        for span in hash_spans:
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

    return "".join(map(lambda x: rjust(hex(x)[2:], 2, '0'), xored))


def solve_used_squares(keystring):
    N = 128
    knot_hashes = [knot_hash(keystring + "-" + str(n)) for n in xrange(N)]
    disk_grid = map(lambda x: bin(int(x, 16))[2:], knot_hashes)
    disk_grid = map(lambda x: rjust(x, 128, '0'), disk_grid)
    counts = map(lambda x: x.count('1'), disk_grid)
    return sum(counts)


def main():
    for line in sys.stdin:
        line = line.strip()
        if line == "":
            break
        print(solve_used_squares(line))


if __name__ == "__main__":
    main()
