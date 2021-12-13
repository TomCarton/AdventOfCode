#!/usr/bin/python3
import sys
from collections import defaultdict

# # Advent of Code 2021
# Day 13

def dots_table(dots, dec = 10):
    width = range(max([a for a, b in dots]) + 1)
    height = range(max([b for a, b in dots]) + 1)

    table = ""
    for y in height:
        if y > 0: table += dec * " "
        for x in width:
            table += "#" if (x, y) in dots else "."
        if y <= height.stop - 2 : table += '\n'
    return table

if __name__ == '__main__':

    filename = 'input.txt'
    if len(sys.argv) > 1:
        filename = sys.argv[1]

    file = open(filename)
    lines = [line.strip() for line in file]

    dots = []
    for line in lines:
        a = line.split(",")

        if a[0] and len(a) == 1:
            line = line.split(" ")

            c, num = line[-1].split("=")
            num = int(num)

            for i in range(len(dots)):
                x, y = dots[i]
                if c == 'x' and x > num:
                    dots[i][0] = num - (x - num)
                elif c== 'y' and y > num:
                    dots[i][1] = num - (y - num)
        elif len(a) == 2:
            dots.append(a)
        else:
            dots = [[int(a), int(b)] for a, b in dots]

    dots.sort()
    dots = [(int(a), int(b)) for a, b in dots]

    # Part One:
    # How many dots are visible after completing just the first fold instruction on your transparent paper?
    print("Part One:", len(set(dots)))

    # Part Two
    # What code do you use to activate the infrared thermal imaging camera system?
    print("Part Two:", dots_table(dots))
