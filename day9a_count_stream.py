#!/usr/bin/env python

import sys


def solve_stream_scoring(line):
    score = 0
    current_score = 0
    n = len(line)
    i = 0
    in_garbage = False
    while i < n:
        c = line[i]
        i += 1
        if c == '!':
            i += 1
            continue
        elif in_garbage:
            if c == '>':
                in_garbage = False
        elif c == '<':
            in_garbage = True
        elif c == '{':
            current_score += 1
            score += current_score
        elif c == '}':
            current_score -= 1
    return score


def main():
    for line in sys.stdin:
        line = line.strip()
        if line == "":
            break
        print(solve_stream_scoring(line))


if __name__ == "__main__":
    main()
