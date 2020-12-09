#!/usr/local/bin/python3.9

from itertools import combinations

# Advent of Code 2020
# Day 09

f = open('input.txt', 'r')
lines = [int(line.strip()) for line in f]

preamble = 25
size = len(lines)

def valid(k, target):
    for i, j in combinations(lines[k - preamble : k], 2):
        if i + j == target:
            return True

    return False

def getWeakness(k, target):
    sum = 0

    buffer = []
    while sum < target:
        buffer.append(lines[k])
        sum += lines[k]
        k += 1

    if sum == target:
        return min(buffer) + max(buffer)


# Part One:
# What is the first number that is not the sum of two of the 25 numbers before it
for i in range(preamble, size):
    if not valid(i, lines[i]):
        invalid = lines[i]
        break

print("Part One:", invalid)


# Part Two:
# What is the encryption weakness in your XMAS-encrypted list of numbers?
for i in range(size):
    weakness = getWeakness(i, invalid)
    if weakness:
        break

print("Part Two:", weakness)
