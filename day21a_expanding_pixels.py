#!/usr/bin/env python

import sys
from math import sqrt


START_LINE = ".#./..#/###"

def rule_to_grid(rule_line):
    return map(list, rule_line.split("/"))


def rotate_grid(grid):
    return [g[::-1] for g in zip(*grid)]


def flip_grid(grid):
    return [r[::-1] for r in grid]


def grid_equal(g1, g2):
    if len(g1) != len(g2):
        return False

    grid1 = map(tuple, g1)
    grid2 = map(tuple, g2)

    return grid1 == grid2


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


def get_grid_size(grid):
    return len(grid)


def split_grid(grid, n):
    if len(grid) == n:
        return [[grid]]

    count = len(grid) / n
    g1 = map(lambda g: [g[i:i+n] for i in xrange(0, len(grid), n)], grid)
    g1 = zip(*g1)
    g2 = map(lambda g: [g[i:i+n] for i in xrange(0, len(g1), n)], g1)
    return g2


def combine_row(row):
    res = []
    for c in row:
        res.extend(c)
    return res


def combine_grids(grids):
    if len(grids) == 1:
        return grids[0][0][:]

    g = map(combine_row, zip(*grids))
    g2 = map(combine_row, zip(*g))
    return g2


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


def count_onoff(grid_row):
    return reduce(lambda (x, y), a: (x + 1, y) if a == "#" else (x, y + 1),
                  grid_row, (0, 0))


def count_pixels(grid):
    row_totals = map(lambda g: count_onoff(g), grid)
    totals = reduce(lambda (a, b), (x, y): (a + x, b + y), row_totals, (0, 0))
    return totals


class Grid(object):
    def __init__(self, line):
        self.grid = rule_to_grid(line)
        self.grid_size = len(self.grid)

    def __repr__(self):
        rows = map(lambda r: "".join(r), self.grid)
        return "/".join(rows)

    def __len__(self):
        return self.grid_size

    def __eq__(self, rhs):
        return self.grid == rhs.grid

    def split(self):
        res = []
        n = len(self)
        r = 2 if n % 2 == 0 else 3
        x = n / r
        rows = []
        for row in self.grid:
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
        g = [g[::-1] for g in zip(*self.grid)]
        line = "/".join(map(lambda s: "".join(s), g))
        return Grid(line)

    def flipped(self):
        g = [r[::-1] for r in self.grid]
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
            sg = map(lambda g: g.grid, s)
            sr = map(lambda g: "".join(map(lambda r: "".join(r), g)), zip(*sg))
            gr.extend(sr)
        line = "/".join(gr)
        return Grid(line)


def solve_expanding_pixels(lines, N):
    rules = parse_rules(lines)
    grid = Grid(START_LINE)

    for _ in xrange(N):
        grid = run_rules(grid, rules)
    on_px, off_px = grid.count_onoff()

    print (on_px, off_px)
    return on_px


def main():
    N = 5
    print(solve_expanding_pixels(sys.stdin.readlines(), N))


if __name__ == "__main__":
    main()
