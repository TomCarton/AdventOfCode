#!/usr/bin/python3

# Advent of Code 2020
# Day 05

f = open('input.txt', 'r')
lines = [line.strip() for line in f]

seats = set()

for line in lines:
    line = line.replace('F', '0').replace('B', '1')
    line = line.replace('L', '0').replace('R', '1')
    seats.add(int(line, 2))

# Part One:
print("Part One:", max(seats))

# Part Two:
print("Part Two:", [x for x in range(min(seats), max(seats) + 1) if x not in seats][0])
