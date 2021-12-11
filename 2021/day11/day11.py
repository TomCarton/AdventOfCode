#!/usr/bin/python3
import sys

# # Advent of Code 2021
# Day 11

def parseOctpus(lines):
    op = {}

    count = 0
    for y, r in enumerate(lines):
        for x, n in enumerate(r):
            op[complex(x, y)] = int(n)
            count += 1

    return op

def dumpOctopus(step, op):
    opstr = ""
    print("Step:", step, "\n----------")
    for i, o in enumerate(op):
        opstr += str(op[o])
        if i % 10 == 9:
            opstr += "\n"
    print(opstr)


if __name__ == '__main__':

    file = open('input.txt')
    lines = [line.strip() for line in file]

    octopus = parseOctpus(lines)

    flash_count = 0
    for k in range(1, 500):
        for o in octopus:
            octopus[o] += 1

        flash_done = set()
        while True:
            for o in octopus:
                if octopus[o] > 9 and o not in flash_done:
                    flash_count += 1
                    flash_done.add(o)

                    for s in -1-1j, 0-1j, 1-1j, \
                             -1+0j,       1+0j, \
                             -1+1j, 0+1j, 1+1j:
                        if o + s in octopus:
                            octopus[o + s] += 1

                    break
            else:
                break

        for o in octopus:
            if octopus[o] > 9:
                octopus[o] = 0

        # Part One:
        # How many total flashes are there after 100 steps?
        if k == 100:
            # dumpOctopus(k, octopus)
            print("Part One:", flash_count)

        # Part Two:
        # What is the first step during which all octopuses flash?
        count = 100
        for o in octopus:
            if octopus[o] == 0:
                count -= 1

        if count == 0:
            # dumpOctopus(k, octopus)
            print("Part Two:", k)
            break
