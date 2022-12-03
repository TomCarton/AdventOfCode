#!/usr/bin/python3
import sys
import os

# Advent of Code 2022
# Day 03

def priority(char):
    c = ord(char)
    if 65 <= c <= 90: return c - 38
    else: return c - 96

def main(filename):
    file = open(filename)
    lines = file.readlines()
    file.close()

    # Part One:
    # Find the item type that appears in both compartments of each rucksack.
    # What is the sum of the priorities of thos item types?

    s = 0
    for line in lines:
        half = len(line) // 2
        first, second = line[:half], line[half:-1]

        letter = (set(first) & set(second)).pop()
        s += priority(letter)

    print("Part One: ", s)

    # Part Two:
    # Find the item type that corresponds to the badges of each three-Elf group. What is the sum of the priorities of those item types?

    s = 0
    for i in range(0, len(lines), 3):
        for letter in lines[i]:
            if letter in lines[i + 1] and letter in lines[i + 2]:
                s += priority(letter)
                break

    print("Part Two: ", s)


# Main
if __name__ == '__main__':
    path = os.path.dirname(os.path.join(os.getcwd(), sys.argv[0]).replace("/./", "/"))

    filename = os.path.join(path, 'input.txt')
    if len(sys.argv) > 1:
        filename = sys.argv[1]

    main(filename)
