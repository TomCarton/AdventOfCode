#!/usr/local/bin/python3.9
import collections
import copy

# Advent of Code 2020
# Day 17

f = open('input.txt', 'r')
lines = [line.strip() for line in f]

# Part One:
# How many cubes are left in the active state after the sixth cycle?
cubes3 = collections.defaultdict(bool)
for x in range(len(lines)):
    for y in range(len(lines[x])):
        if lines[x][y] == '#':
            cubes3[(x, y, 0)] = True

for _ in range(6):
    cubesSource = copy.deepcopy(cubes3)

    points = set()
    for x, y, z in list(cubesSource):
        if cubesSource[(x, y, z)]:
            for xn in range(x - 1, x + 2):
                for yn in range(y - 1, y + 2):
                    points.add((xn, yn, z - 1))
                    points.add((xn, yn, z))
                    points.add((xn, yn, z + 1))

    for x, y, z in points:
        active = cubesSource[(x, y, z)]
        activect = 0

        neighbors = set()
        for xn in range(x - 1, x + 2):
            for yn in range(y - 1, y + 2):
                neighbors.add((xn, yn, z - 1))
                neighbors.add((xn, yn, z))
                neighbors.add((xn, yn, z + 1))
        neighbors.remove((x, y, z))

        for n in neighbors:
            if cubesSource[n]:
                activect += 1

        if active and (activect != 2 and activect != 3):
            cubes3[(x, y, z)] = False
        elif not active and activect == 3:
            cubes3[(x, y, z)] = True

print("Part One:", [i for i in cubes3.values()].count(True))

# Part Two:
# How many cubes are left in the active state after the sixth cycle?
cubes4 = collections.defaultdict(bool)
for x in range(len(lines)):
    for y in range(len(lines[x])):
        if lines[x][y] == '#':
            cubes4[(x, y, 0, 0)] = True

for _ in range(6):
    cubesSource = copy.deepcopy(cubes4)

    points = set()
    for x, y, z, w in list(cubesSource):
        if cubesSource[(x, y, z, w)]:
            for xn in range(x-1, x+2):
                for yn in range(y-1, y+2):
                    for zn in range(z-1, z+2):
                        for wn in range(w-1, w+2):
                            points.add((xn, yn, zn, wn))

    for x, y, z, w in points:
        active = cubesSource[(x, y, z, w)]
        activect = 0

        neighbors = set()
        for xn in range(x-1, x+2):
                for yn in range(y-1, y+2):
                    for zn in range(z-1, z+2):
                        for wn in range(w-1, w+2):
                            neighbors.add((xn, yn, zn, wn))
        neighbors.remove((x, y, z, w))

        for n in neighbors:
            if cubesSource[n]:
                activect += 1

        if active and (activect != 2 and activect != 3):
            cubes4[(x, y, z, w)] = False
        elif not active and activect == 3:
            cubes4[(x, y, z, w)] = True

print("Part Two:", [i for i in cubes4.values()].count(True))
