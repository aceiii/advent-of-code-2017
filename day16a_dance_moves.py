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


def solve_dance_moves(n, moves):
    arr = list(string.ascii_letters[:n])
    for move in moves:
        t = move[:1]
        if t == "s":
            arr = spin(arr, int(move[1:]))
        elif t == "x":
            a, b = map(int, move[1:].split("/"))
            arr = exchange(arr, a, b)
        elif t == "p":
            a, b = move[1:].split("/")
            arr = partner(arr, a, b)
    return "".join(arr)


def main():
    N = 16
    for line in sys.stdin:
        moves = line.strip().split(",")
        print(solve_dance_moves(N, moves))


if __name__ == "__main__":
    main()
