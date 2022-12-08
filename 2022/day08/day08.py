#!/usr/bin/python3
import sys
import os

# Advent of Code 2022
# Day 08

#              west     east    north    south
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

trees = []
side = 0

def is_visible(x, y):
    ht = trees[x][y]
    side = len(trees)

    for dir in directions:
        cx, cy = x, y

        while True:
            cx += dir[0]
            cy += dir[1]

            if cx < 0 or cx >= side or cy < 0 or cy >= side:
                return True;

            h = trees[cx][cy]
            if h >= ht:
                break

    return False

def scenic_score(x, y):
    s = 1
    h = trees[x][y]

    for dx, dy in directions:
        cy, cx, d = x, y, 0
        while 0 <= cx + dx < len(trees[0]) and 0 <= cy + dy < len(trees):
            d += 1

            if trees[cy + dy][cx + dx] >= h:
                break

            cy += dy
            cx += dx

        s *= d

    return s

def main(filename):
    with open(filename) as file:
        for line in file.read().splitlines():
            trees.append(list(map(int, line.strip())))
    side = len(trees)

    # Part One:
    # Consider your map; how many trees are visible from outside the grid?

    count = 4 * (side - 1)
    for y in range(1, len(trees[0]) - 1):
        for x in range(1, len(trees) - 1):
            ht = trees[x][y]

            if is_visible(x, y):
                count += 1

    print("Part One: ", count)

    # Part Two:
    # Consider each tree on your map. What is the highest scenic score possible for any tree?

    highest = max(scenic_score(i, j) for j in range(side) for i in range(side))
    print("Part Two: ", highest)

# Main
if __name__ == '__main__':
    path = os.path.dirname(os.path.join(os.getcwd(), sys.argv[0]).replace("/./", "/"))

    filename = os.path.join(path, 'input.txt')
    if len(sys.argv) > 1:
        filename = sys.argv[1]

    main(filename)
