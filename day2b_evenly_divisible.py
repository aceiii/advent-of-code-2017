#!/usr/bin/env python
# pylint: disable=all

import sys


def find_evenly_divisible(nums):
    n = len(nums)
    sorted_nums = list(reversed(sorted(nums)))
    for i in xrange(n-1):
        a = sorted_nums[i]
        for j in xrange(n-1, i, -1):
            b = sorted_nums[j]
            q, r = divmod(a, b)
            if r == 0:
                return q
            if b > (a / 2):
                break


def evenly_divisible_checksum(sheet):
    line_vals = []

    for line in sheet:
        c = map(int, [c for c in line.strip().split(" ") if c != ""])
        if len(c) == 0:
            continue

        q = find_evenly_divisible(c)
        line_vals.append(q)

    return sum(line_vals)


def main():
    print evenly_divisible_checksum(sys.stdin)


if __name__ == "__main__":
    main()
