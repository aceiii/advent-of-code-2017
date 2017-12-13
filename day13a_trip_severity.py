#!/usr/bin/env python

import sys


def is_caught(k, r):
    s = (r - 1) * 2
    m = s
    while m < k:
        m += s
    return m == k


def solve_trip_severity(layers):
    caught = [k * layers[k] for k in sorted(layers.keys()) if is_caught(k, layers[k])]
    return sum(caught)


def main():
    layers = {}
    for line in sys.stdin:
        depth, layer_range = map(int, line.strip().split(": "))
        layers[depth] = layer_range
    print(solve_trip_severity(layers))


if __name__ == "__main__":
    main()
