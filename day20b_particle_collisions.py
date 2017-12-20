#!/usr/bin/env python

import sys
import operator
from collections import defaultdict


class Vec3(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return "(%d,%d,%d)" % (self.x, self.y, self.z)

    def add_vec(self, vec):
        self.x += vec.x
        self.y += vec.y
        self.z += vec.z

    def manhattan_distance(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

    def as_tuple(self):
        return (self.x, self.y, self.z)


class Particle(object):
    def __init__(self, id_, pos, vel, accel):
        self.id = id_
        self.position = Vec3(*pos)
        self.velocity = Vec3(*vel)
        self.acceleration = Vec3(*accel)
        self.destroyed = False

    def __repr__(self):
        return "{particle_%d %s %s %s}" % (
                    self.id,
                    self.position,
                    self.velocity,
                    self.acceleration)

    def destroy(self):
        self.destroyed = True

    def update(self):
        if self.destroyed:
            return
        self.velocity.add_vec(self.acceleration)
        self.position.add_vec(self.velocity)

    def distance(self):
        return self.position.manhattan_distance()


def load_particles(lines):
    particles = []
    i = 0
    for line in lines:
        line = line.strip()
        if line == "":
            break

        parts = map(lambda s: s.strip()[3:-1], line.split(", "))
        tuples = map(lambda s: tuple(map(int, s.strip().split(","))), parts)
        pos, vel, accel = tuples

        particle = Particle(i, pos, vel, accel)
        particles.append(particle)

        i += 1

    return particles


def solve_colliding_particles(particles):
    i = 0
    while True:
        collision_occurred = False
        positions = defaultdict(lambda: [])

        for p in particles:
            positions[p.position.as_tuple()].append(p)

        for pos, parts in positions.iteritems():
            if len(parts) > 1:
                collision_occurred = True
                for p in parts:
                    p.destroy()

        if collision_occurred:
            particles = filter(lambda p: not p.destroyed, particles)
            i = 0
        else:
            i += 1

        if i > 1000:
            break

        for p in particles:
            p.update()

    return len(particles)


def main():
    particles = load_particles(sys.stdin.readlines())
    print(solve_colliding_particles(particles))


if __name__ == "__main__":
    main()
