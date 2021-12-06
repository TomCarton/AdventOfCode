#!/usr/bin/python3
import sys

# # Advent of Code 2021
# Day 06

if __name__ == '__main__':
    file = open('input.txt')
    lines = [line.strip() for line in file]
    fishes = list(map(int, lines[0].split(",")))

    fishCount = [0] * 9
    for f in fishes:
        fishCount[f] += 1

    # Part One:
    # How many lanternfish would there be after 80 days?
    for _ in range(80):
        newLanterfishes = fishCount[0]

        fishCount = [fishCount[i + 1] for i in range(8)]
        fishCount += [0]

        fishCount[6] += newLanterfishes
        fishCount[8] += newLanterfishes

    print("Part One:", sum(fishCount))

    # Part Two:
    # How many lanternfish would there be after 256 days?
    for _ in range(256 - 80):
        newLanterfishes = fishCount[0]

        fishCount = [fishCount[i + 1] for i in range(8)]
        fishCount += [0]

        fishCount[6] += newLanterfishes
        fishCount[8] += newLanterfishes

    print("Part Two:", sum(fishCount))
