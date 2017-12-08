#!/usr/bin/env python

import sys


def solve_jumps(instr):
    i = 0
    j = 0
    while i >= 0 and i < len(instr):
        c = instr[i]
        instr[i] += 1
        i += c
        j += 1
    return j


def main():
    print(solve_jumps([int(n) for n in sys.stdin if n.strip() != ""]))


if __name__ == "__main__":
    main()
