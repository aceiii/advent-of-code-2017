#!/usr/bin/env python

import sys
from string import rjust


def parent(groups, key):
    if groups[key][0] == key:
        return key
    return parent(groups, groups[key][0])


def union(groups, key, child):
    a = parent(groups, key)
    b = parent(groups, child)

    if a == b:
        return

    if groups[a][1] == groups[b][1]:
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


def union_find_regions(disk_grid):
    N = 128
    regions = {(x, y): ((x, y), 0) for y in xrange(N) for x in xrange(N)}

    for y in xrange(N):
        for x in xrange(N):
            k = (x, y)
            k_val = disk_grid[y][x]
            if x < N-1 and k_val == '1' and disk_grid[y][x + 1] == '1':
                union(regions, k, (x + 1, y))
            if y < N-1 and k_val == '1' and disk_grid[y + 1][x] == '1':
                union(regions, k, (x, y + 1))

    region_map = [[-1 for y in xrange(N)] for x in xrange(N)]
    for y in xrange(N):
        for x in xrange(N):
            if disk_grid[y][x] == '0':
                continue
            px, py = parent(regions, (x, y))
            region_map[y][x] = (py * N) + px

    return region_map


def solve_connected_regions(keystring):
    N = 128
    knot_hashes = [knot_hash(keystring + "-" + str(n)) for n in xrange(N)]
    disk_grid = map(lambda x: bin(int(x, 16))[2:], knot_hashes)
    disk_grid = map(lambda x: rjust(x, 128, '0'), disk_grid)
    region_map = union_find_regions(disk_grid)
    region_set = reduce(lambda x, y: x.union(y), map(set, region_map))
    if -1 in region_set:
        region_set.remove(-1)
    return len(region_set)


def main():
    for line in sys.stdin:
        line = line.strip()
        if line == "":
            break
        print(solve_connected_regions(line))


if __name__ == "__main__":
    main()
