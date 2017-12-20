#!/usr/bin/env python

import sys
import collections
import string


class Duet(object):
    def __init__(self, lines):
        self.instructions = [self.parse_line(line) for line in lines]

    def parse_line(self, line):
        cmd = line.strip().split(" ")
        return (cmd[0], map(self.parse_arg, cmd[1:]))

    def parse_arg(self, arg):
        try:
            return int(arg, 10)
        except ValueError:
            return arg

    def run_to_first_recover(self):
        self.reset_registers()
        while self.is_active() and self.regs["rcv"] is None:
            self.run_instruction()
        return self.regs["rcv"]

    def run_instruction(self):
        instr = self.regs["instr"]
        self.run_cmd(self.instructions[instr])
        self.regs["instr"] += 1

    def run_cmd(self, cmd):
        op, args = cmd
        name = "run_cmd_" + op
        getattr(self, name)(*args)

    def run_cmd_snd(self, x):
        val = self.get_val(x)
        self.regs["snd"] = val

    def run_cmd_set(self, x, y):
        self.regs[x] = self.get_val(y)

    def run_cmd_add(self, x, y):
        self.regs[x] = self.get_val(x) + self.get_val(y)

    def run_cmd_mul(self, x, y):
        self.regs[x] = self.get_val(x) * self.get_val(y)

    def run_cmd_mod(self, x, y):
        self.regs[x] = self.get_val(x) % self.get_val(y)

    def run_cmd_rcv(self, x):
        val = self.get_val(x)
        if val != 0:
            self.regs["rcv"] = self.regs["snd"]

    def run_cmd_jgz(self, x, y):
        val = self.get_val(x)
        offset = self.get_val(y) - 1
        if val > 0:
            self.regs["instr"] += offset

    def get_val(self, x):
        if type(x) is int:
            return x
        return self.regs[x]

    def reset_registers(self):
        self.regs = collections.defaultdict(lambda: 0)
        self.regs["instr"] = 0
        self.regs["snd"] = None
        self.regs["rcv"] = None

    def is_active(self):
        instr = self.regs["instr"]
        return instr >= 0 and instr < len(self.instructions)


def solve_duet_instructions(lines):
    duet = Duet(lines)
    return duet.run_to_first_recover()


def main():
    print(solve_duet_instructions(sys.stdin.readlines()))


if __name__ == "__main__":
    main()
