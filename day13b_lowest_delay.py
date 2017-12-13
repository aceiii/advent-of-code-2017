#!/usr/bin/env python

import sys


def is_caught(k, r):
    s = (r - 1) * 2
    return k % s == 0


def solve_delay_offset(layers):
    offset = 0
    while True:
        c = any(is_caught(k + offset, layers[k]) for k in layers.keys())
        if not c:
            break
        offset += 1
    return offset


def main():
    layers = {}
    for line in sys.stdin:
        depth, layer_range = map(int, line.strip().split(": "))
        layers[depth] = layer_range
    print("answer: %d" % (solve_delay_offset(layers),))


if __name__ == "__main__":
    main()
