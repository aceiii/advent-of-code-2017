#!/usr/bin/env python

import sys


def solve_shortest_hex_path(path):
    dirs = {"n": 0, "s": 0, "ne": 0, "nw": 0, "se": 0, "sw": 0}

    for p in path:
        dirs[p] += 1

    cur_total = -1
    total = sum(dirs.values())
    while cur_total != total:
        cur_total = total

        while dirs["sw"] > 0 and dirs["n"] > 0:
            dirs["sw"] -= 1
            dirs["n"] -= 1
            dirs["nw"] += 1

        while dirs["se"] > 0 and dirs["n"] > 0:
            dirs["se"] -= 1
            dirs["n"] -= 1
            dirs["ne"] += 1

        while dirs["ne"] > 0 and dirs["s"] > 0:
            dirs["ne"] -= 1
            dirs["s"] -= 1
            dirs["se"] += 1

        while dirs["nw"] > 0 and dirs["s"] > 0:
            dirs["nw"] -= 1
            dirs["s"] -= 1
            dirs["sw"] += 1

        while dirs["sw"] > 0 and dirs["se"] > 0:
            dirs["sw"] -= 1
            dirs["se"] -= 1
            dirs["s"] += 1

        while dirs["nw"] > 0 and dirs["ne"] > 0:
            dirs["nw"] -= 1
            dirs["ne"] -= 1
            dirs["n"] += 1

        while dirs["nw"] > 0 and dirs["se"] > 0:
            dirs["nw"] -= 1
            dirs["se"] -= 1

        while dirs["ne"] > 0 and dirs["sw"] > 0:
            dirs["ne"] -= 1
            dirs["sw"] -= 1

        while dirs["n"] > 0 and dirs["s"] > 0:
            dirs["n"] -= 1
            dirs["s"] -= 1

        total = sum(dirs.values())

    return cur_total


def main():
    for line in sys.stdin:
        line = line.strip()
        if line == "":
            break
        print(solve_shortest_hex_path([s for s in line.strip().split(",") if s != ""]))

if __name__ == "__main__":
    main()
