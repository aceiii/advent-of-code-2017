#!/usr/bin/env python

import sys
import re

def hash_bank(banks):
    return " ".join(map(str, banks))


def redistribute_memory(banks):
    # get highest index
    n = len(banks)
    idx = 0
    mx = banks[idx]
    for i in xrange(1, n):
        b = banks[i]
        if b > mx:
            idx = i
            mx = b

    # redistribute
    banks[idx] = 0
    while mx > 0:
        mx -= 1
        idx = (idx + 1) % n
        banks[idx] += 1

    return banks


def solve_memory_reallocation(banks):
    t = 0
    s = set()
    m = {}
    h = hash_bank(banks)
    m[h] = t
    print h
    while h not in s:
        m[h] = t
        t += 1
        s.add(h)
        banks = redistribute_memory(banks)
        h = hash_bank(banks)
    return t - m[h]

def main():
    banks = map(int, (b for b in re.split("\\s", sys.stdin.readline().strip()) if b != ""))
    print(solve_memory_reallocation(banks))


if __name__ == "__main__":
    main()
