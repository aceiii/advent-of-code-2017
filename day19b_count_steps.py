#!/usr/bin/env python

import sys


def find_start(lines):
    first_line = lines[0]
    for i in xrange(len(first_line)):
        if first_line[i] == "|":
            return i

    raise Exception("no start")


def parse_tubes(lines):
    tubes = {}

    for y in xrange(len(lines)):
        line = lines[y]
        for x in xrange(len(line)):
            c = line[x].strip()
            if c == "":
                continue
            tubes[(x, y)] = c

    return tubes


def possible_next_nodes(tubes, node, direction):
    nodes = []
    if direction == "all" or direction == "down":
        next_node = (node[0], node[1] + 1)
        if next_node in tubes:
            nodes.append(next_node)
    if direction == "all" or direction == "up":
        next_node = (node[0], node[1] - 1)
        if next_node in tubes:
            nodes.append(next_node)
    if direction == "all" or direction == "left":
        next_node = (node[0] - 1, node[1])
        if next_node in tubes:
            nodes.append(next_node)
    if direction == "all" or direction == "right":
        next_node = (node[0] + 1, node[1])
        if next_node in tubes:
            nodes.append(next_node)

    return nodes


def get_next_node(tubes, node, direction):
    if tubes[node] == "+":
        prev_node = None
        if direction == "down":
            prev_node = (node[0], node[1] - 1)
        elif direction == "up":
            prev_node = (node[0], node[1] + 1)
        elif direction == "left":
            prev_node = (node[0] + 1, node[1])
        elif direction == "right":
            prev_node = (node[0] - 1, node[1])

        nodes = possible_next_nodes(tubes, node, "all")
        possible_nodes = filter(lambda n: n != prev_node, nodes)
        if len(possible_nodes) > 0:
            next_node = possible_nodes[0]
            new_dir = None

            if next_node == (node[0], node[1] - 1):
                new_dir = "up"
            elif next_node == (node[0], node[1] + 1):
                new_dir = "down"
            elif next_node == (node[0] - 1, node[1]):
                new_dir = "left"
            elif next_node == (node[0] + 1, node[1]):
                new_dir = "right"

            return (next_node, new_dir)

    next_node = possible_next_nodes(tubes, node, direction)
    if len(next_node) > 0:
        return (next_node[0], direction)

    return None


def trace_tube_path(tubes, start_x):
    cur_node = (start_x, 0)
    cur_dir = "down"
    path = [cur_node]
    while True:
        next_node_result = get_next_node(tubes, cur_node, cur_dir)
        if next_node_result is None:
            break
        cur_node, cur_dir = next_node_result
        path.append(cur_node)
    return path


def trace_path_letters(tubes, path):
    letters = []
    for p in path:
        c = tubes[p]
        if c != "|" and c != "-" and c != "+":
            letters.append(c)
    return letters


def solve_tube_maze_step_count(lines):
    start_x = find_start(lines)
    tubes = parse_tubes(lines)
    path = trace_tube_path(tubes, start_x)
    return len(path)


def main():
    print(solve_tube_maze_step_count(sys.stdin.readlines()))


if __name__ == "__main__":
    main()
