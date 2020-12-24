#!/usr/local/bin/python3.9
from copy import deepcopy

# Advent of Code 2020
# Day 24

# e 65 0110 0101
# n 6e 0110 1110
# s 73 0111 0011
# w 77 0111 0111

f = open('input.txt', 'r')
lines = [line.strip() for line in f]

neighborship = [(-1, -1), (-1, 1), (0, -2), (0, 2), (1, -1), (1, 1)]

# Part One:
# how many tiles are left with the black side up?

flipped = dict()

for line in lines:
    tiles = []
    i = 0
    while i < len(line):
        if line[i] == 'e' or line[i] == 'w':
            tiles.append(line[i])
            i += 1
        else:
            tiles.append(line[i:i + 2])
            i += 2

    x, y = 0, 0
    for t in tiles:
        if t[-1] == 'e':
            y -= 1
            if len(t) == 1:
                y -= 1
            elif t[0] == 'n':
                x -= 1
            elif t[0] == 's':
                x += 1

        elif t[-1] == 'w':
            y += 1
            if len(t) == 1:
                y += 1
            elif t[0] == 'n':
                x -= 1
            elif t[0] == 's':
                x += 1

    flipped[(x, y)] = True if (x,y) not in flipped else not flipped[(x, y)]

print('Part One:', sum(flipped.values()))

# Part Two:
# How many tiles will be black after 100 days?

for _ in range(100):
    tmp = deepcopy(flipped)
    
    sides = dict()
    for x, y in flipped:
        if flipped[(x, y)]:
            for dx, dy in neighborship:
                x2, y2 = x + dx, y + dy
                sides[(x2, y2)] = sides.get((x2, y2), 0) + 1

    for flip in flipped:
        if flipped[flip]:
            if flip not in sides or sides[flip] > 2:
                tmp[flip] = False

    for tile in sides:
        if tile not in flipped or not flipped[tile]:
            if sides[tile] == 2:
                tmp[tile] = True

    flipped = tmp

print('Part Two:', sum(flipped.values()))
