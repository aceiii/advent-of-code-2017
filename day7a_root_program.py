#!/usr/bin/env python

import sys

from collections import defaultdict


def solve_root_program(lines):
    counts = defaultdict(lambda: 0)
    for line in lines:
        line = line.strip()
        if line == "":
            continue

        vals = line.strip().split("->")
        name = vals[0].strip().split(" ")[0].strip()

        counts[name] += 1

        if len(vals) > 1:
            second = vals[1].strip()
            children = map(lambda s: s.strip(), second.strip().split(","))

            for child in children:
                counts[child] -= 1

    root = filter(lambda (k, v): v == 1, counts.iteritems())
    return root[0]


def main():
    print(solve_root_program(sys.stdin))


if __name__ == "__main__":
    main()
