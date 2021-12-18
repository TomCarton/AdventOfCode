#!/usr/bin/python3
import sys
import math, random

# # Advent of Code 2021
# Day 18

def get_id():
    return random.randrange(0, 1000000)


def parse(line, pos=0):
    if line[pos] == "[":
        node = {'parent': None, 'id': get_id()}
        left, pos = parse(line, pos + 1)
        node['left'] = left
        if not 'val' in left:
            left['parent'] = node

        if line[pos] == ',':
            pos += 1
        else:
            print("parse error")
            exit(1)

        right, pos = parse(line, pos)
        node['right'] = right
        if not 'val' in right:
            right['parent'] = node

        if line[pos] == ']':
            pos += 1
        else:
            print("parse error")
            exit(1)

        return node, pos
    else:
        chars = []
        while line[pos] >= '0' and line[pos] <= '9':
            chars += line[pos]
            pos += 1

        return {'val': int("".join(chars))}, pos

def add_to_left(node, val):
    changed = False

    parent = node['parent']
    while parent != None and not 'val' in (parent['left']) and parent['left']['id'] == node['id']:
        node = parent
        parent = parent['parent']

    if parent != None:
        node = parent

        if 'val' in node['left']:
            node['left']['val'] += val
        else:
            node = parent['left']

            while not 'val' in node['right']:
                node = node['right']

            node['right']['val'] += val

def add_to_right(node, val):
    parent = node['parent']
    while parent != None and not 'val' in parent['right'] and parent['right']['id'] == node['id']:
        node = parent
        parent = parent['parent']

    if parent != None:
        node = parent

        if 'val' in node['right']:
            node['right']['val'] += val
        else:
            node = parent['right']

            while not 'val' in node['left']:
                node = node['left']

            node['left']['val'] += val

def explode(node, depth=0):
    if 'val' in node:
        return node, False

    left = node['left']

    node['left'], changed_left = explode(left, depth + 1)
    if changed_left:
        return node, True

    left = node['left']
    right = node['right']

    if depth > 3 and 'val' in left and 'val' in right:
        add_to_left(node, left['val'])
        add_to_right(node, right['val'])

        return {'val': 0}, True

    node['right'], changed_right = explode(right, depth + 1)

    return node, changed_right


def split(node):
    if 'val' in node:
        return node, False

    left = node['left']
    if 'val' in left and left['val'] >= 10:
        node['left'] = {
            'left': {
                'val': left['val'] // 2
            },
            'right': {
                'val': (math.ceil(left['val'] / 2))
            },
            'parent': node,
            'id': get_id()
        }
        return node, True
    else:
        node['left'], changed_left = split(node['left'])
        if changed_left:
            return node, True

    right = node['right']
    if 'val' in right and right['val'] >= 10:
        node['right'] = {
            'left': {
                'val': right['val'] // 2
            },
            'right': {
                'val': (math.ceil(right['val'] / 2))
            },
            'parent': node,
            'id': get_id()
        }
        return node, True
    else:
        node['right'], changed_right = split(node['right'])
        if changed_right:
            return node, True

    return node, False


def magnitude(node):
    if 'val' in node:
        return node['val']

    return 3 * magnitude(node['left']) + 2 * magnitude(node['right'])


def expand(root):
    changed = True
    while changed:
        _, changed = explode(root)
        if not changed:
            _, changed = split(root)

    return root


def add(numbers):
    root = None
    for number in numbers:
        new, _ = parse(number)
        if root == None:
            root = new
            root['parent'] = None
        else:
            root = {'left': root, 'right': new, 'parent': None, 'id': get_id()}
            root['left']['parent'] = root
            root['right']['parent'] = root

        expand(root)

    return magnitude(root)

if __name__ == '__main__':
    filename = 'input.txt'
    if len(sys.argv) > 1:
        filename = sys.argv[1]

    file = open(filename)
    lines = [line.strip() for line in file]

    # Part One:
    # What do you get if you multiply the score of the losing player by the number of times the die was rolled during the game?
    print("Part One:", add(lines))

    # Part Two:
    #
    highest = 0

    for i in range(0, len(lines)):
        for j in range(0, len(lines)):
            if i == j:
                continue
            val = add([lines[i], lines[j]])
            highest = max(highest, val)

    print("Part Two:", highest)
