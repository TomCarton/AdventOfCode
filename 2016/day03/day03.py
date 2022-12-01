#!/usr/bin/python3
import sys
import os
import re

# Advent of Code 2016
# Day 03

def main(filename):
    file = open(filename)
    lines = file.readlines()
    file.close()

    # Part Onw:
    # How many of the listed triangles are possible?

    possible = 0
    for line in lines:
        sides = [int(v) for v in re.findall(r'\d+', line)]
        side = sorted(sides)
        if side[0] + side[1] > side[2]:
            possible += 1

    print("Part One:", possible)

    # Part Two:
    # How many of the listed triangles are possible?

    data = [[int(v) for v in re.findall(r'\d+', line)] for line in lines]

    possible = 0
    for i in range(0, len(data), 3):
        for j in range(0, len(data[i])):
            # side = [data[i][j], data[i+1][j], data[i+2][j]]
            side = sorted([data[i][j], data[i+1][j], data[i+2][j]])
            if side[0] + side[1] > side[2]:
                possible += 1

    print("Part Two:", possible)

# Main
if __name__ == '__main__':
    path = os.path.dirname(os.path.join(os.getcwd(), sys.argv[0]).replace("/./", "/"))

    filename = os.path.join(path, 'input.txt')
    if len(sys.argv) > 1:
        filename = sys.argv[1]

    main(filename)
