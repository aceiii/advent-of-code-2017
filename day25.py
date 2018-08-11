#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import sys
import re


class TuringMachine(object):
    def __init__(self, lines):
        self.states = {}
        self.tape = [0] * 1024
        self.pos = 512

        # first line: Begin in state A.
        match = re.match(r"Begin in state (\w+)\.", lines[0])
        self.current_state = match.group(1)

        # second line: Perform a diagnostic checksum after 6 steps.
        match = re.match(r"Perform a diagnostic checksum after (\d+) steps\.",
                         lines[1])
        self.checksum = int(match.group(1))

        line_no = 3
        while line_no < len(lines):
            # line_no + 0: In state A:
            state_name = re.match(r"In state (\w+)\:", lines[line_no]).group(1)

            # line_no + 1: If the current value is 0:

            # line_no + 2:    - Write the value 1.
            match = re.match(r"    - Write the value (\d)\.",
                             lines[line_no + 2])
            write_value1 = int(match.group(1))

            # line_no + 3:    - Move one slot to the right.
            match = re.match(r"    - Move one slot to the (\w+).",
                             lines[line_no + 3])
            move_dir1 = match.group(1)

            # line_no + 4:    - Continue with state B.
            match = re.match(r"    - Continue with state (\w+).",
                             lines[line_no + 4])
            goto_state1 = match.group(1)

            # line_no + 5:  If the current value is 1:

            # line_no + 6:    - Write the value 0.
            match = re.match(r"    - Write the value (\d)\.",
                             lines[line_no + 6])
            write_value2 = int(match.group(1))

            # line_no + 7:    - Move one slot to the left.
            match = re.match(r"    - Move one slot to the (\w+).",
                             lines[line_no + 7])
            move_dir2 = match.group(1)

            # line_no + 8:    - Continue with state B.
            match = re.match(r"    - Continue with state (\w+).",
                             lines[line_no + 8])
            goto_state2 = match.group(1)

            zero_instr = (write_value1,
                          -1 if move_dir1 == 'left' else 1,
                          goto_state1)

            one_instr = (write_value2,
                         -1 if move_dir2 == 'left' else 1,
                         goto_state2)

            self.states[state_name] = (zero_instr, one_instr)

            line_no += 10


    def diagnostic(self):
        return sum(self.tape)

    def run(self):
        for i in xrange(self.checksum):
            state = self.states[self.current_state]

            write_value, move_dir, goto_state = state[self.tape[self.pos]]

            self.tape[self.pos] = write_value
            self.pos += move_dir
            if self.pos < 0:
                self.tape = ([0] * 1024) + self.tape
                self.pos += 1024
            self.current_state = goto_state


def main(lines):
    machine = TuringMachine(lines)
    machine.run()
    print(machine.diagnostic())


if __name__ == "__main__":
    main(sys.stdin.readlines())
