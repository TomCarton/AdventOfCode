#!/usr/bin/python3
import sys

# # Advent of Code 2021
# Day 05

if __name__ == '__main__':
    file = open('input.txt')
    lines = [line.strip() for line in file]

    # Part One:
    #

    di = {}
    for line in lines:
        s1, s2 = line.split(' -> ')
        x1, y1 = map(int, s1.split(','))
        x2, y2 = map(int, s2.split(','))

        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                di[(x1, y)] = 1 if (x1, y) not in di else di[(x1, y)] + 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                di[(x, y1)] = 1 if (x, y1) not in di else di[(x, y1)] + 1

    print( "Part One:", len([each for each in di if di[each] > 1]) )

    # Part Two:
    #

    di = {}
    for line in lines:
        s1, s2 = line.split(' -> ')
        x1, y1 = map(int, s1.split(','))
        x2, y2 = map(int, s2.split(','))

        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                di[(x1, y)] = 1 if (x1, y) not in di else di[(x1, y)] + 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                di[(x, y1)] = 1 if (x, y1) not in di else di[(x, y1)] + 1
        elif abs(x1-x2) == abs(y1-y2):
            dx = -1 if x1 > x2 else 1
            dy = -1 if y1 > y2 else 1
            x, y = x1, y1
            while 1:
                di[(x, y)] = 1 if (x, y) not in di else di[(x, y)] + 1
                if (x, y) == (x2, y2): break
                x += dx
                y += dy

    print( "Part Two:", len([each for each in di if di[each] > 1]))
