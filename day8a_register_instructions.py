#!/usr/bin/env python

import sys
import re

from operator import itemgetter, lt, gt, le, ge, eq, ne, add, sub
from collections import defaultdict


class Instruction(object):
    ops = {
        "<": lt,
        ">": gt,
        "<=": le,
        ">=": ge,
        "==": eq,
        "!=": ne,
        "inc": add,
        "dec": sub,
    }

    def __init__(self, instr, cond):
        self.instr = map(lambda s: s.strip(), instr)
        self.cond = map(lambda s: s.strip(), cond)
        pass

    def check_condition(self, registers):
        reg, op, val = self.cond
        reg_val = registers[reg]
        int_val = int(val)
        return self.ops[op](reg_val, int_val)

    def run_instruction(self, registers):
        reg, op, val = self.instr
        reg_val = registers[reg]
        int_val = int(val)
        registers[reg] = self.ops[op](reg_val, int_val)

    def run(self, registers):
        if self.check_condition(registers):
            self.run_instruction(registers)


def parse_line(line):
    instr, cond = [s for s in line.strip().split("if") if s != ""]
    instrs = tuple([s for s in re.split("\\s", instr.strip()) if s != ""])
    conds = tuple([s for s in re.split("\\s", cond.strip()) if s != ""])
    return Instruction(instrs, conds)


def solve_jump_instructions(lines):
    instructions = [parse_line(line) for line in lines]

    registers = defaultdict(lambda: 0)
    for instr in instructions:
        instr.run(registers)

    r = sorted(registers.iteritems(), key=itemgetter(1), reverse=True)
    return r[0]


def main():
    print(solve_jump_instructions(sys.stdin))


if __name__ == "__main__":
    main()
