#!/usr/bin/env python3
import sys

dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))

input_filename = "input.txt"
if len(sys.argv) > 1 and sys.argv[1]:
    input_filename = sys.argv[1]
data = open(input_filename)

lines = [[int(k) for k in x.strip()] for x in data.readlines()]

# Part One:
#
p1 = 0
for i, line in enumerate(lines):
    for j, val in enumerate(line):
        if val == 0:
            q = {(i, j)}
            nextQ = set()
            for k in range(1,10):
                for (x, y) in q:
                    for dir in dirs:
                        newX, newY = x + dir[0], y + dir[1]
                        if 0 <= newX < len(lines) and 0 <= newY < len(lines[0]) and lines[newX][newY] == k:
                            nextQ.add((newX, newY))
                q = nextQ
                nextQ = set()
            p1 += len(q)
print("  Part One:", p1)

# Part Two:
#
p2 = 0
for i, line in enumerate(lines):
    for j, val in enumerate(line):
        if val == 0:
            q = {(i, j, (i, j))}
            nextQ = set()
            for k in range(1,10):
                for (x, y, path) in q:
                    for dir in dirs:
                        newX, newY = x + dir[0], y + dir[1]
                        if 0 <= newX < len(lines) and 0 <= newY < len(lines[0]) and lines[newX][newY] == k:
                            nextQ.add((newX, newY, path + (newX, newY)))
                q = nextQ
                nextQ = set()
            p2 += len(q)
print("  Part Two:", p2)
