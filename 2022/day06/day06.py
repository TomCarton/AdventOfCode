#!/usr/bin/python3
import sys
import os

# Advent of Code 2022
# Day 06

def main(filename):
    file = open(filename)
    lines = file.readlines()
    file.close()

    line = lines[0]

    # Part One:
    # 
    for k in range(0, len(line)):
        c4 = line[k:k + 4]
        cs4 = set(c4)
        if len(c4) == len(cs4):
            break

    print("Part One: ", k + 4)

    # Part Two:
    # 

    for k in range(0, len(line)):
        c4 = line[k:k + 14]
        cs4 = set(c4)
        if len(c4) == len(cs4):
            break

    print("Part Two: ", k + 14)


# Main
if __name__ == '__main__':
    path = os.path.dirname(os.path.join(os.getcwd(), sys.argv[0]).replace("/./", "/"))

    filename = os.path.join(path, 'input.txt')
    if len(sys.argv) > 1:
        filename = sys.argv[1]

    main(filename)
