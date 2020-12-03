#!/bin/env/python

# # Advent of Code 2020
# Day 03

f = open('input.txt', 'r')
lines = [line.strip() for line in f]

w, h = len(lines[0]), len(lines)

result = 0
slopes = [(3, 1), (1, 1), (5, 1), (7, 1), (1, 2)]
for dx, dy in slopes:
    x, y = 0, 0

    treeCount = 0
    while y < h:
        treeCount += lines[y][x] == '#'

        x = (x + dx) % w
        y += dy

    if (result == 0):
        result = treeCount
        print("Part One:", result)
    else:
        result *= treeCount

print("Part Two:", result)
