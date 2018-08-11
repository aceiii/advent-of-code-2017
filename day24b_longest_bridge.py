#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import sys
from operator import itemgetter


class Piece(object):
    def __init__(self, line, index):
        ports = tuple(sorted(map(int, line.strip().split("/"))))

        self.piece_id = index

        self.left_port = ports[0]
        self.right_port = ports[1]
        self.is_used = False

    def __repr__(self):
        return "Piece:{0} ({1}/{2}) {3}".format(self.piece_id,
                                            self.left_port,
                                            self.right_port,
                                            '-' if self.is_used else '')

    def __getitem__(self, index):
        return self.left_port if index == 0 else self.right_port


def piece_has_available_port(piece, port_number):
    return piece.is_used is False and (
        piece.left_port == port_number or piece.right_port == port_number
    )


class PieceMap(object):
    def __init__(self, pieces):
        self.pieces = pieces
        self.ports = {}

        for index, piece in enumerate(self.pieces):
            if piece.left_port in self.ports:
                self.ports[piece.left_port].append(index)
            else:
                self.ports[piece.left_port] = [index]

            if piece.right_port in self.ports:
                self.ports[piece.right_port].append(index)
            else:
                self.ports[piece.right_port] = [index]

    def __repr__(self):
        pass

    def get_pieces_for_port(self, port_number):
        if port_number in self.ports:
            ports = [self.pieces[p_id] for p_id in self.ports[port_number]]
            return filter(lambda p: piece_has_available_port(p, port_number),
                          ports)
        return []


def find_longest_bridge(piece_map, bridge = [0]):
    port_number = bridge[-1]
    available_pieces = piece_map.get_pieces_for_port(port_number)

    if not available_pieces:
        return bridge

    result = bridge

    for piece in available_pieces:
        piece.is_used = True

        new_bridge = bridge[:]

        if piece.left_port == port_number:
            new_bridge.append(piece.left_port)
            new_bridge.append(piece.right_port)
        else:
            new_bridge.append(piece.right_port)
            new_bridge.append(piece.left_port)

        result_bridge = find_longest_bridge(piece_map, new_bridge)

        if len(result_bridge) > len(result) or (
                len(result_bridge) == len(result) and
                sum(result_bridge) > sum(result)):
            result = result_bridge

        piece.is_used = False

    return result


def main(lines):
    pieces = [Piece(line, index) for (index, line) in enumerate(lines)]
    piece_map = PieceMap(pieces)
    bridge = find_longest_bridge(piece_map)
    print("Answer: {}, bridge: {}".format(sum(bridge), bridge))


if __name__ == "__main__":
    main(sys.stdin.readlines())
