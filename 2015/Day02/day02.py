#!/usr/local/bin/python3.10
import sys

def main():
    file = open('input.txt')

    paper = 0
    ribbon = 0

    for line in file:
        sides = [eval(i) for i in line.strip().split('x')]
        sides = sorted(sides)

        paper = paper + 3 * sides[0] * sides[1] + 2 * sides [1] * sides [2] + 2 * sides [0] * sides [2]

        ribbon = ribbon + 2 * sides[0] + 2 * sides[1]
        ribbon = ribbon + sides[0] * sides[1] * sides[2]

    # Part One:
    # How many total square feet of wrapping paper should they order?
    print("Part One:", paper)

    # Part Two:
    # How many total square feet of wrapping paper should they order?
    print("Part Two:", ribbon)

    return 0

if __name__ == '__main__':
    sys.exit(main()) 
