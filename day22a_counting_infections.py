#!/usr/bin/env python

import sys
from collections import defaultdict
from operator import itemgetter


FACINGS = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def clean_lines(lines):
    return [s.strip() for s in lines if s.strip() != ""]


def parse_infection_map(lines):
    infection = defaultdict(lambda: False)
    for y in xrange(len(lines)):
        line = lines[y]
        for x in xrange(len(line)):
            c = line[x]
            pos = (x, y)
            infection[pos] = True if c == "#" else False
    return infection


def turn_left(face):
    i = FACINGS.index(face)
    return FACINGS[(i - 1) % len(FACINGS)]


def turn_right(face):
    i = FACINGS.index(face)
    return FACINGS[(i + 1) % len(FACINGS)]


def solve_infection_count(lines, n, debug):
    infection = parse_infection_map(lines)
    size = (len(lines[0]), len(lines))

    pos = (size[0] / 2, size[1] / 2)
    face = (0, -1)

    if debug:
        print_map(infection, pos)

    count = 0
    for _ in xrange(n):
        if infection[pos]:
            face = turn_right(face)
        else:
            face = turn_left(face)
            count += 1

        infection[pos] = not infection[pos]
        pos = tuple(map(sum, zip(pos, face)))

        if debug:
            print_map(infection, pos)

    return count


def print_map(infection, pos):
    items = filter(lambda (k, v): v, infection.iteritems())
    keys = map(itemgetter(0), items)
    vals = zip(*keys)
    min_x, min_y = map(lambda a: min(a) - 2, vals)
    max_x, max_y = map(lambda a: max(a) + 2, vals)

    pos_x, pos_y = pos
    for y in xrange(min_y, max_y + 1):
        line = ""
        for x in xrange(min_x, max_x + 1):
            line += "#" if infection[(x, y)] else "."
            line += "[" if (x + 1) == pos_x and y == pos_y else " "
            line += "]" if x == pos_x and y == pos_y else " "
        print line
    print


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 10000
    debug = bool(sys.argv[2]) if len(sys.argv) > 2 else False
    lines = clean_lines(sys.stdin.readlines())
    print(solve_infection_count(lines, n, debug))


if __name__ == "__main__":
    main()
