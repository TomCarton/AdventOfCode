#!/usr/bin/python3
import sys
import os

# Advent of Code 2022
# Day 01

def main(filename):
    file = open(filename, 'r')
    data = file.read()
    file.close()

    elves = [sum([int(calories) for calories in elf.split('\n')]) for elf in data.split('\n\n')]
    elves.sort(reverse = True)

    # Part One:
    # Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
    print("Part One:", elves[0])

    # Part Two:
    # Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
    print("Part Two:", sum(elves[0:3]))


# Main
if __name__ == '__main__':
    path = os.path.dirname(os.path.join(os.getcwd(), sys.argv[0]).replace("/./", "/"))

    filename = os.path.join(path, 'input.txt')
    if len(sys.argv) > 1:
        filename = sys.argv[1]

    main(filename)
