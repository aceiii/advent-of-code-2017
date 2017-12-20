#!/usr/bin/env python

import sys
import collections
from Queue import deque


class Duet(object):
    def __init__(self, lines, program_id):
        self.program_id = program_id
        self.instructions = [self.parse_line(line) for line in lines]
        self.reset_registers()
        self.reset_queue()
        self.waiting = False

    def __repr__(self):
        r = str(dict(self.regs))
        q = str(list(self.queue))
        w = str(self.waiting)
        return ",".join([r, q, w])

    def link(self, duet):
        self.duet = duet

    def send(self, val):
        self.queue.append(val)

    def parse_line(self, line):
        cmd = line.strip().split(" ")
        return (cmd[0], tuple(map(self.parse_arg, cmd[1:])))

    def parse_arg(self, arg):
        try:
            return int(arg, 10)
        except ValueError:
            return arg

    def run_instruction(self):
        if not self.is_active():
            return

        instr = self.regs["instr"]
        offset = self.run_cmd(self.instructions[instr])
        self.regs["instr"] += offset

    def run_cmd(self, cmd):
        op, args = cmd
        name = "run_cmd_" + op
        result = getattr(self, name)(*args)
        return result

    def run_cmd_snd(self, x):
        val = self.get_val(x)
        self.duet.send(val)
        self.regs["snd"] += 1
        return 1

    def run_cmd_set(self, x, y):
        self.regs[x] = self.get_val(y)
        return 1

    def run_cmd_add(self, x, y):
        self.regs[x] = self.get_val(x) + self.get_val(y)
        return 1

    def run_cmd_mul(self, x, y):
        self.regs[x] = self.get_val(x) * self.get_val(y)
        return 1

    def run_cmd_mod(self, x, y):
        self.regs[x] = self.get_val(x) % self.get_val(y)
        return 1

    def run_cmd_rcv(self, x):
        try:
            self.waiting = True
            val = self.queue.popleft()
            self.regs[x] = val
            self.waiting = False
            return 1
        except IndexError:
            return 0

        val = self.get_val(x)
        if val != 0:
            self.regs["rcv"] = self.regs["snd"]
        return 1

    def run_cmd_jgz(self, x, y):
        val = self.get_val(x)
        if val > 0:
            return self.get_val(y)
        return 1

    def get_val(self, x):
        if type(x) is int:
            return x
        return self.regs[x]

    def reset_registers(self):
        self.regs = collections.defaultdict(lambda: 0)
        self.regs["instr"] = 0
        self.regs["p"] = self.program_id

    def reset_queue(self):
        self.queue = deque()

    def is_active(self):
        instr = self.regs["instr"]
        return instr >= 0 and instr < len(self.instructions)

    def is_waiting(self):
        return self.waiting and len(self.queue) < 1


def solve_duet_instructions(lines):
    d1 = Duet(lines, 0)
    d2 = Duet(lines, 1)

    d1.link(d2)
    d2.link(d1)

    while True:
        # print("d1", d1)
        # print("d2", d2)

        d1.run_instruction()
        d2.run_instruction()

        if d1.is_waiting() and d2.is_waiting():
            break

        if not d1.is_active() and not d2.is_active():
            break

    return d2.regs["snd"]


def main():
    print(solve_duet_instructions(sys.stdin.readlines()))


if __name__ == "__main__":
    main()
