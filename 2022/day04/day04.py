#!/usr/bin/python3
import sys
import os
import re

# Advent of Code 2022
# Day 04

def main(filename):
    file = open(filename)
    lines = file.readlines()
    file.close()

    # Part One:
    # In how many assignment pairs does one range fully contain the other?

    count = 0
    for line in lines:
        elf1, elf2 = line.split(',')

        (m1, M1) = map(int, elf1.split('-'))
        (m2, M2) = map(int, elf2.split('-'))

        count += (m1 <= m2 <= M2 <= M1) or (m2 <= m1 <= M1 <= M2)

    print("Part One: ", count)

    # Part Two:
    # Instead, the Elves would like to know the number of pairs that overlap at all.

    count = 0
    for line in lines:
        elf1, elf2 = line.split(',')

        (m1, M1) = map(int, elf1.split('-'))
        (m2, M2) = map(int, elf2.split('-'))

        count += (m1 <= m2 <= M1) or (m2 <= m1 <= M2)

    print("Part Two: ", count)


# Main
if __name__ == '__main__':
    path = os.path.dirname(os.path.join(os.getcwd(), sys.argv[0]).replace("/./", "/"))

    filename = os.path.join(path, 'input.txt')
    if len(sys.argv) > 1:
        filename = sys.argv[1]

    main(filename)
