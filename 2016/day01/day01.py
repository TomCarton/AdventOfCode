#!/usr/bin/python3

import sys
import os
#import itertools as itt

# Advent of Code 2022
# Day {day:02}

def main(filename):
    f = open(filename, 'r')
    data = f.read()
    f.close()

    axes = ((0, 1), (1, 0), (0, -1), (-1, 0))
    direction = 0

    position = (0, 0)

    places = set()
    # places.add(tuple(position))

    for command in data.split(', '):
        if command[0] == 'L':
            direction = (direction - 1) % 4
        elif command[0] == 'R':
            direction = (direction + 1) % 4

        multiplier = int(command[1:])

        position = (position[0] + axes[direction][0] * multiplier, position[1] + axes[direction][1] * multiplier)

    # Part One:
    # 

    dist = sum([abs(coordinate) for coordinate in position])
    print("Part One: ", dist)

    # Part Two:
    # 

    position = (0, 0)

    places = set()
    places.add(position)

    for command in data.split(', '):
        if command[0] == 'L':
            direction = (direction - 1) % 4
        elif command[0] == 'R':
            direction = (direction + 1) % 4

        multiplier = int(command[1:])
        for step in range(multiplier):
            position = (position[0] + axes[direction][0], position[1] + axes[direction][1])

            if position in places:
                print(sum([abs(coordinate) for coordinate in position]))
                exit(0)

            places.add(position)


    print("Part Two: ")


# Main
if __name__ == '__main__':
    path = os.path.dirname(os.path.join(os.getcwd(), sys.argv[0]).replace("/./", "/"))

    filename = os.path.join(path, 'input.txt')
    if len(sys.argv) > 1:
        filename = sys.argv[1]

    main(filename)