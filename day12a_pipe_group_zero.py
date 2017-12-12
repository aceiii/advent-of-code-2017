#!/usr/bin/env python

import sys


def parent(groups, key):
    if groups[key][0] == key:
        return key
    return parent(groups, groups[key][0])


def union(groups, key, child):
    a = parent(groups, key)
    b = parent(groups, child)

    if a == b:
        return

    if groups[a][1] < groups[b][1]:
        p, r = groups[a]
        groups[a] = (b, r)
    elif groups[a][1] > groups[b][1]:
        p, r = groups[b]
        groups[b] = (a, r)
    else:
        ap, ar = groups[a]
        bp, br = groups[b]
        groups[b] = (a, br)
        groups[a] = (ap, ar + 1)


def solve_pipe_zero(pipes):
    n = max(pipes.keys())
    groups = [(i, 0) for i in xrange(n+1)]

    for k, children in pipes.iteritems():
        for child in children:
            union(groups, k, child)

    result = [i for i in xrange(n+1) if parent(groups, i) == parent(groups, 0)]
    return len(result)


def main():
    pipes = {}
    for line in sys.stdin:
        line = line.strip()
        if line == "":
            break
        parts = line.strip().split(" <-> ")
        key = int(parts[0])
        children = map(int, parts[1].split(","))
        pipes[key] = children

    print(solve_pipe_zero(pipes))


if __name__ == "__main__":
    main()
