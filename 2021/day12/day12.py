#!/usr/bin/python3
import sys
from collections import defaultdict, Counter

# # Advent of Code 2021
# Day 12

def visit(i, v, b):
    if i.islower() and v[i]:
        if i == 'start' or b:
            return 0
        b = True

    if i == 'end':
        return 1

    count = 0

    v[i] += 1
    for j in caves[i]:
        count += visit(j, v, b)
    v[i] -= 1

    return count

if __name__ == '__main__':

    filename = 'input.txt'
    if len(sys.argv) > 1:
        filename = sys.argv[1]

    file = open(filename)
    lines = [line.strip() for line in file]

    caves = defaultdict(list)
    for line in lines:
        left, right = line.split('-')
        caves[left].append(right)
        caves[right].append(left)

    # Part One:
    # How many paths through this cave system are there that visit small caves at most once?
    print("Part One:", visit('start', Counter(), True))

    # Part Two:
    # Given these new rules, how many paths through this cave system are there?
    print("Part Two:", visit('start', Counter(), False))
