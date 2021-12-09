#!/usr/bin/python3

# # Advent of Code 2021
# Day 09

file = open('input.txt')
lines = [line.strip() for line in file]

dp = [(-1, 0), (1, 0), (0, -1), (0, 1)]

checked = set()

def basin_size_at(x, y):
    size = 0
    if (x, y) not in checked:
        checked.add((x, y))

        hp = int(lines[y][x])
        if hp < 9:
            size = 1
            for dx, dy in dp:
                if x + dx in range(len(lines[0])) and y + dy in range(len(lines)):
                    size += basin_size_at(x + dx, y + dy)

    return size

if __name__ == '__main__':
    # Part One:
    # What is the sum of the risk levels of all low points on your heightmap?

    sum = 0
    for x in range(len(lines)):
        for y in range(len(lines[0])):
            hp = int(lines[y][x])

            low = True
            for dx, dy in dp:
                if x + dx in range(len(lines[0])) and y + dy in range(len(lines)):
                    hdp = int(lines[y + dy][x + dx])

                    if hp >= hdp:
                        low = False

            if low:
                sum += hp + 1

    print("Part One:", sum)

    # Part Two:
    # What do you get if you multiply together the sizes of the three largest basins?

    basin_sizes = []
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            size = basin_size_at(x, y)
            if size > 0:
                basin_sizes.append(size)

    basin_sizes.sort()

    print("Part Two:", basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3])
