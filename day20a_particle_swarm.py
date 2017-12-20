#!/usr/bin/env python

import sys
import operator


def add3(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


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


class Particle(object):
    def __init__(self, id_, pos, vel, accel):
        self.id = id_
        self.position = Vec3(*pos)
        self.velocity = Vec3(*vel)
        self.acceleration = Vec3(*accel)

    def __repr__(self):
        return "{particle_%d %s %s %s}" % (
                    self.id,
                    self.position,
                    self.velocity,
                    self.acceleration)

    def update(self):
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


def solve_closes_particle(particles):
    for i in xrange(5000):
        for p in particles:
            p.update()

    nearest_particles = sorted(particles,
                               key=operator.methodcaller("distance"),
                               reverse=True)

    return nearest_particles[-1]


def main():
    particles = load_particles(sys.stdin.readlines())
    print(solve_closes_particle(particles))


if __name__ == "__main__":
    main()
