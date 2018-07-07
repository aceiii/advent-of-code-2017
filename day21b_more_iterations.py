#!/usr/bin/env python

import sys
from math import sqrt


START_LINE = ".#./..#/###"

def grid_equal(g1, g2):
    if len(g1) != len(g2):
        return False

    grid1 = map(tuple, g1)
    grid2 = map(tuple, g2)

    return grid1 == grid2


def parse_rules(lines):
    rules = []

    for line in lines:
        line = line.strip()
        if line == "":
            continue

        first, second = map(lambda s: s.strip(), line.split("=>"))
        matcher = GridMatcher(first, second)
        rules.append(matcher)

    return rules


def run_rules(grid, rules):
    grids = grid.split()
    new_grids = []
    for g in grids:
        matched_rules = filter(lambda r: r.match(g), rules)
        if len(matched_rules) > 0:
            new_grids.append(matched_rules[0].grid())
        else:
            raise Exception("wtf", rules)
            new_grids.append(g)
    return Grid.join(new_grids)


class GridMatcher(object):
    def __init__(self, input_rule, output_rule):
        self.output_rule = output_rule

        grid = Grid(input_rule)
        self.grids = [grid, grid.flipped()]
        for _ in xrange(3):
            new_grid = grid.rotated()
            self.grids.append(new_grid)
            self.grids.append(new_grid.flipped())
            grid = new_grid

    def match(self, grid):
        matches = filter(lambda g: g == grid, self.grids)
        return len(matches) > 0

    def grid(self):
        return Grid(self.output_rule)


class Grid(object):
    def __init__(self, line):
        self.line = line
        self.grid_size = len(self.grid())

    def __repr__(self):
        rows = map(lambda r: "".join(r), self.grid)
        return "/".join(rows)

    def __len__(self):
        return self.grid_size

    def __eq__(self, rhs):
        return self.line == rhs.line

    def grid(self):
        return map(tuple, self.line.split("/"))

    def split(self):
        res = []
        n = len(self)
        r = 2 if n % 2 == 0 else 3
        x = n / r
        rows = []
        for row in self.grid():
            gr = [row[i:i+r] for i in xrange(0, n, r)]
            rows.append(gr)
        zrows = zip(*rows)
        for j in xrange(0, n, r):
            for i in xrange(x):
                gr = map(lambda r: "".join(r), zrows[i][j:j+r])
                g = "/".join(gr)
                res.append(Grid(g))
        return res

    def rotated(self):
        g = [g[::-1] for g in zip(*self.grid())]
        line = "/".join(map(lambda s: "".join(s), g))
        return Grid(line)

    def flipped(self):
        g = [r[::-1] for r in self.grid()]
        line = "/".join(map(lambda s: "".join(s), g))
        return Grid(line)

    def count_onoff(self):
        line = str(self)
        return (line.count("#"), line.count("."))

    @staticmethod
    def join(grid_arr):
        n = int(sqrt(len(grid_arr)))
        r = len(grid_arr[0])
        gr = []
        for i in xrange(0, n * n, n):
            s = grid_arr[i:i+n]
            sg = map(lambda g: g.grid(), s)
            sr = map(lambda g: "".join(map(lambda r: "".join(r), g)), zip(*sg))
            gr.extend(sr)
        line = "/".join(gr)
        return Grid(line)


def solve_expanding_pixels(lines, N):
    rules = parse_rules(lines)
    grid = Grid(START_LINE)

    for i in xrange(N):
        print i
        grid = run_rules(grid, rules)

    on_px, off_px = grid.count_onoff()

    print (on_px, off_px)
    return on_px


def main():
    N = 18
    print(solve_expanding_pixels(sys.stdin.readlines(), N))


if __name__ == "__main__":
    main()
