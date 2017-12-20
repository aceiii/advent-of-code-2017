#!/usr/bin/env python

import sys
import string


def spin(arr, x):
    return arr[-x:] + arr[:-x]


def exchange(arr, a, b):
    ret = arr[:]
    ret[a], ret[b] = ret[b], ret[a]
    return ret


def partner(arr, a, b):
    a_index = arr.index(a)
    b_index = arr.index(b)
    return exchange(arr, a_index, b_index)


class Spin(object):
    def __init__(self, n):
        self.n = n

    def run(self, arr):
        return spin(arr, self.n)


class Exchange(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def run(self, arr):
        return exchange(arr, self.a, self.b)


class Partner(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def run(self, arr):
        return partner(arr, self.a, self.b)


class DanceProgram(object):
    def __init__(self, n):
        self.n = n
        self.i = 0

    def add_moves(self, moves):
        self.moves = []
        for m in moves:
            t = m[:1]
            if t == "s":
                x = int(m[1:])
                self.moves.append((t, x))
            elif t == "x":
                a, b = map(int, m[1:].split("/"))
                self.moves.append((t, (a, b)))
            elif t == "p":
                a, b = m[1:].split("/")
                self.moves.append((t, (a, b)))
            else:
                raise Exception("Invalid move: '" + m + "'")

    def spin(self, x):
        self.i = (self.i + x) % self.n

    def exchange(self, a, b):
        x = (a - self.i) % self.n
        y = (b - self.i) % self.n
        self.arr[x], self.arr[y] = self.arr[y], self.arr[x]

    def partner(self, a, b):
        self.arr[a], self.arr[b] = self.arr[b], self.arr[a]

    def build(self):
        self.arr = list(string.ascii_letters[:self.n])
        result_set = set([self.result()])
        results = [self.result()]
        while True:
            for t, x in self.moves:
                if t == "s":
                    self.arr = spin(self.arr, x)
                elif t == "x":
                    a, b = x
                    self.arr = exchange(self.arr, a, b)
                else:
                    a, b = x
                    self.arr = partner(self.arr, a, b)
            res = self.result()
            if res in result_set:
                break
            results.append(res)
            result_set.add(res)
        self.results = results

    def result(self):
        return "".join(self.arr)

    def run(self, m):
        return self.results[m % len(self.results)]


def solve_repeating_dance(n, m, moves):
    dance = DanceProgram(n)
    dance.add_moves(moves)
    dance.build()
    print dance.results
    print dance.results[0] == dance.results[-1]
    return dance.run(m)


def main():
    N = 16
    M = 10**9
    for line in sys.stdin:
        moves = line.strip().split(",")
        print(solve_repeating_dance(N, M, moves))


if __name__ == "__main__":
    main()
