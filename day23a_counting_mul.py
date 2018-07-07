#!/usr/bin/env python

import sys
from collections import defaultdict


def tryInt(i):
    try:
        return int(i)
    except ValueError:
        return i


class Instruction(object):
    def __init__(self, line):
        self.cmd = map(tryInt, line.strip().split(" "))

    def do(self, program):
        op = self.cmd[0]
        name = "do_" + op
        method = getattr(self, name)
        program.incr_op_count(op)
        return method(program, *self.cmd[1:])

    def do_set(self, program, x, y):
        program.set_register(x, program.get_value(y))

    def do_sub(self, program, x, y):
        x_val = program.get_value(x)
        y_val = program.get_value(y)
        program.set_register(x, x_val - y_val)

    def do_mul(self, program, x, y):
        x_val = program.get_value(x)
        y_val = program.get_value(y)
        program.set_register(x, x_val * y_val)

    def do_jnz(self, program, x, y):
        x_val = program.get_value(x)
        y_val = program.get_value(y)
        return y_val if x_val != 0 else None


class Program(object):
    def __init__(self, instructions):
        self.instructions = instructions
        self.reset()

    def reset(self):
        self.op_count = defaultdict(lambda: 0)
        self.registers = defaultdict(lambda: 0)

    def run(self):
        while not self.done():
            i = self.instr_ptr()
            instr = self.instructions[i]
            o = instr.do(self)
            self.incr_instr_ptr(o if o is not None else 1)

    def set_register(self, x, y):
        self.registers[x] = y

    def instr_ptr(self):
        return self.registers["instr"]

    def incr_instr_ptr(self, i):
        self.registers["instr"] += i

    def incr_op_count(self, op):
        self.op_count[op] += 1

    def get_value(self, x):
        if type(x) is str:
            return self.registers[x]
        return x

    def done(self):
        i = self.instr_ptr()
        return i < 0 or i >= len(self.instructions)

    def counts(self):
        return self.op_count.copy()


def parse_instructions(lines):
    instructions = []
    for line in sys.stdin:
        line = line.strip()
        if line == "":
            break
        instructions.append(Instruction(line))
    return instructions


def solve_mul_count(lines):
    instructions = parse_instructions(sys.stdin)
    program = Program(instructions)
    program.run()
    return program.counts()["mul"]


def main():
    print(solve_mul_count(sys.stdin))


if __name__ == "__main__":
    main()
