#!/usr/bin/python3
import os
import sys
from copy import deepcopy

# Advent of Code 2022
# Day 05

def parseInput(lines):
    count = len(lines[0]) // 4

    stacks = count * [None]
    for k in range(count):
        stacks[k] = []
    directives = []

    for line in lines:
        if line.strip():
            if not line.startswith('move'):
                # stacks line
                for k in range(count):
                    c = line[4 * k + 1]

                    if c.isalpha():
                        stacks[k].insert(0, c)
            else:
                # directive
                directives.append(line.rstrip())

    return stacks, directives

def dumpStacks(stacks):
    height = 0
    for stack in stacks:
        height = max(height, len(stack))

    for h in range(height, -1, -1):
        for stack in stacks:
            c = '   '
            if len(stack) > h:
                c = '[{}]'.format(stack[h])

            print(c, end = ' ')

        print('')

    for n in range(1, len(stacks) + 1):
        print(' {} '.format(n), end = ' ')

    print('\n')

def topCrates(stacks):
    return ''.join(stack[-1] for stack in stacks)


def main(filename):
    file = open(filename)
    lines = file.readlines()
    file.close()

    initial_stacks, directives = parseInput(lines)
    dumpStacks(initial_stacks)

    # Part One:
    # After the rearrangement procedure completes, what crate ends up on top of each stack?

    stacks = deepcopy(initial_stacks)
    for directive in directives:
        if directive:
            d = directive.split()
            count = int(d[1])
            source = int(d[3]) - 1
            target = int(d[5]) - 1

            stacks[target].extend(stacks[source][-count:][::-1])
            del stacks[source][-count:]

    print("Part One:", topCrates(stacks))

    # Part Two:
    # After the rearrangement procedure completes, what crate ends up on top of each stack?

    stacks = deepcopy(initial_stacks)
    for directive in directives:
        if directive:
            d = directive.split()
            count = int(d[1])
            source = int(d[3]) - 1
            target = int(d[5]) - 1

            stacks[target].extend(stacks[source][-count:])
            del stacks[source][-count:]

    print("Part Two:", topCrates(stacks))

# Main
if __name__ == '__main__':
    path = os.path.dirname(os.path.join(os.getcwd(), sys.argv[0]).replace("/./", "/"))

    filename = os.path.join(path, 'input.txt')
    if len(sys.argv) > 1:
        filename = sys.argv[1]

    main(filename)
