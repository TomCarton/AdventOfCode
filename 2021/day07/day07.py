#!/usr/bin/python3
import sys

# # Advent of Code 2021
# Day 07

if __name__ == '__main__':
    file = open('input.txt')
    lines = [line.strip() for line in file]
    crabs = list(map(int, lines[0].split(",")))

    # Part One:
    # How much fuel must they spend to align to that position?

    minFuel = sys.maxsize

    for i in crabs:
        cost = 0

        for j in crabs:
            cost += abs(i - j)

        minFuel = min(cost, minFuel)

    print( "Part One: {:d}".format( minFuel ) )

    # Part Two:
    # How much fuel must they spend to align to that position?

    minFuel = sys.maxsize

    for i in range(min(crabs), max(crabs) + 1):
        cost = 0

        for j in crabs:
            delta = abs(i - j)
            cost += (delta * (delta + 1)) // 2

        minFuel = min(cost, minFuel)

    print( "Part Two: {:d}".format( minFuel ) )
