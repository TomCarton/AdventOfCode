#!/usr/bin/python3
import itertools as itt

# # Advent of Code 2021
# Day 02

file = open('input.txt')
lines = [line.strip() for line in file]

if __name__ == '__main__':

    # Part One:
    # What do you get if you multiply your final horizontal position by your final depth?
    horizontal = 0
    depth = 0
    for l in lines:
        if l.startswith("down"):
            depth += int(l[5:])
        if l.startswith("up"):
            depth -= int(l[3:])

        if l.startswith("forward"):
            horizontal += int(l[8:])

    print( "Part One: {:d}".format(horizontal * depth) )

    # Part Two:
    # What do you get if you multiply your final horizontal position by your final depth?
    horizontal = 0
    depth = 0
    aim = 0
    for l in lines:
        if l.startswith("down"):
            aim += int(l[5:])
        if l.startswith("up"):
            aim -= int(l[3:])

        if l.startswith("forward"):
            target = int(l[8:])
            horizontal += target
            depth += target * aim

    print( "Part Two: {:d}".format(horizontal * depth) )
