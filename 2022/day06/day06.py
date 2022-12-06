#!/usr/bin/python3
import sys
import os

# Advent of Code 2022
# Day 06

def markerStart(s, n):
    for k in range(len(s)):
        if len(set(s[k:k + n])) == n:
            return k + n

def main(filename):
    file = open(filename)
    lines = file.readlines()
    file.close()

    line = lines[0]

    # Part One:
    # How many characters need to be processed before the first start-of-packet marker is detected?

    print("Part One: ", markerStart(lines[0], 4))

    # Part Two:
    # How many characters need to be processed before the first start-of-message marker is detected?

    print("Part Two: ", markerStart(lines[0], 14))


# Main
if __name__ == '__main__':
    path = os.path.dirname(os.path.join(os.getcwd(), sys.argv[0]).replace("/./", "/"))

    filename = os.path.join(path, 'input.txt')
    if len(sys.argv) > 1:
        filename = sys.argv[1]

    main(filename)
