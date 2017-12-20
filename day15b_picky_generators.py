#!/usr/bin/env python

import sys


class Gen(object):
    def __init__(self, start, factor, modulo, multiple):
        self.prev = start
        self.factor = factor
        self.modulo = modulo
        self.multiple = multiple

    def next(self):
        while True:
            self.prev = (self.prev * self.factor) % self.modulo
            if self.prev % self.multiple == 0:
                break
        return self.prev


def lower16_match(a, b):
    return (a & 0xffff) == (b & 0xffff)


def solve_dueling_generator(a_start, b_start, N):
    R = 2147483647
    FA = 16807
    FB = 48271
    MA = 4
    MB = 8

    A = Gen(a_start, FA, R, MA)
    B = Gen(b_start, FB, R, MB)

    count = 0
    for _ in xrange(N):
        a = A.next()
        b = B.next()
        if lower16_match(a, b):
            count += 1

    return count


def main():
    N = 5 * (10**6)
    lines = [line for line in sys.stdin.readlines() if line.strip() != '']
    a, b = map(lambda s: int(s.rsplit(" ", 1)[-1]), lines[:2])
    print(solve_dueling_generator(a, b, N))


if __name__ == "__main__":
    main()
