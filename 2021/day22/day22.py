#!/usr/bin/python3
import sys
import re

# # Advent of Code 2021
# Day 22

def get_subrange(crange, low, high):
    c0, c1 = crange[0], crange[-1]
    if c1 < low or c0 > high:
        return []

    c0 = min(c0, high)
    c0 = max(c0, low)
    c1 = min(c1, high)
    c1 = max(c1, low)

    return range(c0, c1 + 1)

def count_uninterrupted(item, rest):
    _, xr, yr, zr = item
    total = len(xr) * len(yr) * len(zr)

    conflicts = []
    ref_val = 0

    for item in rest:
        state, xr2, yr2, zr2 = item

        xsr = get_subrange(xr2, xr[0], xr[-1])
        if len(xsr) == 0:
            continue

        ysr = get_subrange(yr2, yr[0], yr[-1])
        if len(ysr) == 0:
            continue

        zsr = get_subrange(zr2, zr[0], zr[-1])
        if len(zsr) == 0:
            continue

        conflicts.append((state, xsr, ysr, zsr))
        ref_val += len(xsr) * len(ysr) * len(zsr)

    for i, item in enumerate(conflicts):
        total -= count_uninterrupted(item, conflicts[i + 1:])

    return total

if __name__ == '__main__':
    filename = 'input.txt'
    if len(sys.argv) > 1:
        filename = sys.argv[1]

    file = open(filename)
    lines = [line.strip() for line in file]

    data = list(parse(lines))

    # Part One:
    # Afterward, considering only cubes in the region x=-50..50,y=-50..50,z=-50..50, how many cubes are on?
    cubes = {}
    for item in data:
        state, xr, yr, zr = item
        for x in get_subrange(xr, -50, 50):
            for y in get_subrange(yr, -50, 50):
                for z in get_subrange(zr, -50, 50):
                    cubes[x, y, z] = state

    print("Part One:", sum(1 for state in cubes.values() if state == 'on'))

    # Part Two:
    # Starting again with all cubes off, execute all reboot steps. Afterward, considering all cubes, how many cubes are on?
    count = 0
    for i, item in enumerate(data):
        state, xr, yr, zr = item
        if state == 'on':
            count += count_uninterrupted(item, data[i + 1:])

    print("Part Two:", count)
