#!/usr/bin/env python3

import sys

def check_mas(chars: list[str]) -> bool:
    return "".join(chars) == "MAS"

input_filename = "input.txt"
if len(sys.argv) > 1 and sys.argv[1]:
    input_filename = sys.argv[1]

lines = open(input_filename).readlines()

# Part One:
#
p1 = 0

data = []
for line in lines:
    data.append(line.strip())

for row in range(len(data)):
    for col in range(len(data[row])):
        char = data[row][col]
        if char == "X":
            if row > 2:
                if check_mas(
                    [data[row - 1][col], data[row - 2][col], data[row - 3][col]]
                ):
                    p1 += 1
            if col > 2:
                if check_mas(
                    [data[row][col - 1], data[row][col - 2], data[row][col - 3]]
                ):
                    p1 += 1
            if col < len(data[row]) - 3:
                if check_mas(
                    [data[row][col + 1], data[row][col + 2], data[row][col + 3]]
                ):
                    p1 += 1
            if row > 2 and col > 2:
                if check_mas(
                    [
                        data[row - 1][col - 1],
                        data[row - 2][col - 2],
                        data[row - 3][col - 3],
                    ]
                ):
                    p1 += 1
            if row > 2 and col < len(data[row]) - 3:
                if check_mas(
                    [
                        data[row - 1][col + 1],
                        data[row - 2][col + 2],
                        data[row - 3][col + 3],
                    ]
                ):
                    p1 += 1
            if row < len(data) - 3:
                if check_mas(
                    [data[row + 1][col], data[row + 2][col], data[row + 3][col]]
                ):
                    p1 += 1
            if row < len(data) - 3 and col > 2:
                if check_mas(
                    [
                        data[row + 1][col - 1],
                        data[row + 2][col - 2],
                        data[row + 3][col - 3],
                    ]
                ):
                    p1 += 1
            if row < len(data) - 3 and col < len(data[row]) - 3:
                if check_mas(
                    [
                        data[row + 1][col + 1],
                        data[row + 2][col + 2],
                        data[row + 3][col + 3],
                    ]
                ):
                    p1 += 1

print("  Part One:", p1)


# Part Two:
#
p2 = 0

data = []
for line in lines:
    data.append(line.strip())

for row in range(1, len(data) - 1):
    for col in range(1, len(data[row]) - 1):
        if data[row][col] == "A":
            if (
                check_mas(
                    [data[row - 1][col - 1], data[row][col], data[row + 1][col + 1]]
                )
                or check_mas(
                    [data[row + 1][col + 1], data[row][col], data[row - 1][col - 1]]
                )
            ) and (
                check_mas(
                    [data[row - 1][col + 1], data[row][col], data[row + 1][col - 1]]
                )
                or check_mas(
                    [data[row + 1][col - 1], data[row][col], data[row - 1][col + 1]]
                )
            ):
                p2 += 1

print("  Part Two:", p2)
