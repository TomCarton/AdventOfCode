#!/usr/bin/python3
import sys
import re

# # Advent of Code 2021
# Day 17

if __name__ == '__main__':
    filename = 'input.txt'
    if len(sys.argv) > 1:
        filename = sys.argv[1]

    file = open(filename)
    lines = [line.strip() for line in file]

    # -- target area: x=253..280, y=-73..-46
    x1, x2, y1, y2 = map(int, re.findall(r"-?[0-9]+", lines[0]))

    best = -1000
    count = 0

    for yvel in range(y1, 300):
        for xvel in range(x2 + 1):
            hy = 0
            px, py = 0, 0
            vx, vy = xvel, yvel

            while True:
                px += vx; py += vy
                vx -= (vx > 0) - (vx < 0); vy -= 1
                hy = max(hy, py)

                if x1 <= px <= x2 and y1 <= py <= y2:
                    count += 1
                    best = max(best, hy)
                    break

                if py < y1 or px > x2:
                    break

    # Part One:
    # What is the highest y position it reaches on this trajectory?
    print("Part One:", best)

    # Part Two:
    # How many distinct initial velocity values cause the probe to be within the target area after any step?
    print("Part Two:", count)
