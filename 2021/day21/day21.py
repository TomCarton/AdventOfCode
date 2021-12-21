#!/usr/bin/python3
import sys
from itertools import cycle, islice, product

# # Advent of Code 2021
# Day 21

def quantic_play(p1, s1, p2, s2, pool = {}):
    key = (p1, s1, p2, s2)
    if key in pool:
        return pool[key]

    sc = (0, 0)
    for r in product((1, 2, 3), repeat = 3):
        r = sum(r)
        np = (p1 + r - 1) % 10 + 1
        ns = s1 + np

        i, j = 0, 1
        if ns < 21:
            i, j = quantic_play(p2, s2, np, ns)
        sc = (sc[0] + j, sc[1] + i)

    pool[key] = sc
    return sc

if __name__ == '__main__':
    filename = 'input.txt'
    if len(sys.argv) > 1:
        filename = sys.argv[1]

    file = open(filename)
    lines = [line.strip() for line in file]

    start_p1 = int(lines[0][28:])
    start_p2 = int(lines[1][28:])

    # Part One:
    # What do you get if you multiply the score of the losing player by the number of times the die was rolled during the game?

    p = [start_p1, start_p2]
    sc = [0, 0]

    rolls = 0
    dice = iter(cycle(range(1, 101)))

    turn = 0
    while max(sc) < 1000:
        p[turn] = (p[turn] + sum(list(islice(dice, 3))) - 1) % 10 + 1
        sc[turn] += p[turn]

        rolls += 3
        turn = 1 - turn

    print("Part One:", min(sc) * rolls)

    # Part Two:
    # Find the player that wins in more universes; in how many universes does that player win?

    p = [start_p1, start_p2]
    sc = [0, 0]

    print("Part Two:", max(quantic_play(p[0], sc[0], p[1], sc[1])))
