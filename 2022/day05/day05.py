#!/usr/bin/python3
import sys
import os

def parseInput(lines):
    count = len(lines[0]) // 4

    stacks = count * [None]
    for k in range(count):
        stacks[k] = []

    for line in lines:
        if line.strip() and not line.startswith('move'):
            for k in range(count):
                c = line[4 * k + 1]

                if c.isalpha():
                    stacks[k].insert(0, c)
    return stacks

def dumpStacks(stacks):
    height = 0
    for stack in stacks:
        height = max(height, len(stack))

    for h in range(height, 0, -1):
        for stack in stacks:
            c = '   '
            if len(stack) > h:
                c = '[{}]'.format(stack[h])

            print(c, end = ' ')

        print('')

    for n in range(1, len(stacks) + 1):
        print(' {} '.format(n), end = ' ')

    print('\n')

# Advent of Code 2022
# Day 05

def main(filename):
    file = open(filename)
    lines = file.readlines()
    file.close()

    # [H] [Q] [P] [L] [G] [V] [Z] [D] [B]
    # 1   2   3   4   5   6   7   8   9 

    # move 2 from 7 to 2

    stacks = parseInput(lines)

    # print(stacks)
    dumpStacks(stacks)

    # Part One:
    # 

    print("Part One: ")

    # Part Two:
    # 

    print("Part Two: ")


# Main
if __name__ == '__main__':
    path = os.path.dirname(os.path.join(os.getcwd(), sys.argv[0]).replace("/./", "/"))

    filename = os.path.join(path, 'input.txt')
    if len(sys.argv) > 1:
        filename = sys.argv[1]

    main(filename)
