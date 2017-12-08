#!/usr/bin/env python

import sys


def sorted_string(s):
    return "".join(sorted(s))


def is_valid_passphrase(line):
    s = set()
    words = (w for w in line.strip().split(" ") if w != "")
    for w in words:
        w = sorted_string(w)
        if w in s:
            return False
        s.add(w)
    return True


def main():
    total = 0
    for line in sys.stdin:
        line = line.strip()
        if line == "":
            break
        valid = is_valid_passphrase(line)
        total += 1 if valid else 0
        print(line, valid)
    print(total)


if __name__ == "__main__":
    main()
