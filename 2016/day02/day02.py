#!/usr/bin/python3
import sys
import os

# Advent of Code 2016
# Day 02

keyboard1 = [[1, 4, 7],
             [2, 5, 8],
             [3, 6, 9]]

keyboard2 = [[' ', ' ', '1', ' ', ' '],
             [' ', '2', '3', '4', ' '],
             ['5', '6', '7', '8', '9'],
             [' ', 'A', 'B', 'C', ' '],
             [' ', ' ', 'D', ' ', ' ']]

def main(filename):
    file = open(filename)
    lines = file.readlines()
    file.close()

    # Part One:
    # What is the first bathroom code?

    x, y = 1, 1

    code = ""
    for line in lines:
        for c in line.rstrip():
            if   c == 'L': x = max(0, x - 1)
            elif c == 'R': x = min(x + 1, 2)
            elif c == 'U': y = max(0, y - 1)
            elif c == 'D': y = min(y + 1, 2)

        code += str(keyboard1[x][y])

    print("Part One:", code)

    # Part Two:
    # What is the second bathroom code?

    x, y = 0, 2

    code = ""
    for line in lines:
        for c in line.rstrip():
            nx, ny = x, y

            if   c == 'L': nx = max(0, nx - 1)
            elif c == 'R': nx = min(nx + 1, 4)
            elif c == 'U': ny = max(0, ny - 1)
            elif c == 'D': ny = min(ny + 1, 4)


            if keyboard2[nx][ny] != ' ':
                x, y = nx, ny

        code +=str(keyboard2[y][x])

    print("Part Two:", code)

# Main
if __name__ == '__main__':
    path = os.path.dirname(os.path.join(os.getcwd(), sys.argv[0]).replace("/./", "/"))

    filename = os.path.join(path, 'input.txt')
    if len(sys.argv) > 1:
        filename = sys.argv[1]

    main(filename)
