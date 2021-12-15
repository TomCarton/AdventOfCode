#!/usr/bin/python3
import sys
from itertools import product
from heapq import heappush, heappop

# # Advent of Code 2021
# Day 15

def get_map_from(lines):
    return { (x, y): int(val)
            for y, line in enumerate(lines)
                for x, val in enumerate(line) }

def expand_map(map, size):
    expanded_map = dict()

    l = max(map)[0] + 1
    for dy in range(size):
        for dx in range(size):
            for (x, y), val in map.items():
                v = val + dx + dy
                if v > 9: v -= 9

                expanded_map[(x + dx * l, y + dy * l)] = v

    return expanded_map

def neighbours(x, y):
    for dy, dx in product((-1, 0, 1), repeat = 2):
        if (abs(dx) != abs(dy)):
            yield (x + dx, y + dy)

def navigate(risk_map):
    start = min(risk_map)
    q = [(0, start)]

    end = max(risk_map)
    heuristic = lambda x, y: abs(x - y) <= end[0] // 3

    risk = -1
    risks = dict()
    while q:
        risk, pt = heappop(q)

        if pt == end:
            break

        for nb in neighbours(*pt):
            if nc := risk_map.get(nb):
                c = risk + nc
                if c < risks.get(nb, 9999) and heuristic(*nb):
                    risks[nb] = c
                    heappush(q, (c, nb))

    return risk

if __name__ == '__main__':
    filename = 'input.txt'
    if len(sys.argv) > 1:
        filename = sys.argv[1]

    file = open(filename)
    lines = [line.strip() for line in file]

    risk_map = get_map_from(lines)

    # Part One:
    # What is the lowest total risk of any path from the top left to the bottom right?
    print("Part One:", navigate(risk_map))

    # Part Two:
    #
    risk_map = expand_map(risk_map, 5)
    print("Part Two:", navigate(risk_map))
