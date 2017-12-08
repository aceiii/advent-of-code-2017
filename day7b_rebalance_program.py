#!/usr/bin/env python

import sys

from collections import defaultdict


def total_weight(weights, edges, node):
    w = weights[node]
    if node not in edges:
        return w
    for c in edges[node]:
        w += total_weight(weights, edges, c)
    return w


def solve_root_program(lines):
    counts = defaultdict(lambda: 0)
    weights = {}
    edges = {}
    for line in lines:
        line = line.strip()
        if line == "":
            continue

        vals = line.strip().split("->")
        name = vals[0].strip().split(" ")[0].strip()

        weight = int(vals[0].strip().split(" ")[1].strip("(").strip(")"))
        weights[name] = weight

        counts[name] += 1

        if len(vals) > 1:
            second = vals[1].strip()
            children = map(lambda s: s.strip(), second.strip().split(","))
            edges[name] = children

            for child in children:
                counts[child] -= 1

    root = filter(lambda (k, v): v == 1, counts.iteritems())[0][0]

    found = False
    node = root
    diff = 0
    while not found:
        cw = [(c, total_weight(weights, edges, c)) for c in edges[node]]
        ws = [w for c, w in cw]
        dw = filter(lambda (c, w): ws.count(w) == 1, cw)
        if len(dw) == 0:
            found = True
            break
        diff = filter(lambda (c, w): ws.count(w) != 1, cw)[0][1]
        node = dw[0][0]

    weight = total_weight(weights, edges, node)
    # print diff
    # print total_weight(weights, edges, node)
    # print weights[node]
    # print diff - weight
    return weights[node] + (diff - weight)


def main():
    print(solve_root_program(sys.stdin))


if __name__ == "__main__":
    main()
