#!/usr/bin/python3
import sys
from collections import Counter

# # Advent of Code 2021
# Day 14

def get_polymer_from(template):
    polymer = {}

    for i in range(0, len(template) - 1):
        pair = template[i:i+2]
        polymer[pair] = 1 if pair not in polymer else polymer[pair] + 1

    return polymer

def step(polymer, rules):
    new_polymer = {}

    for pair, count in polymer.items():
        np1 = pair[0] + rules[pair]
        np2 = rules[pair] + pair[-1]
        new_polymer[np1] = count if np1 not in new_polymer else new_polymer[np1] + count
        new_polymer[np2] = count if np2 not in new_polymer else new_polymer[np2] + count

    return new_polymer

def get_quantity_delta(template, polymer):
    count = {}
    count[template[-1]] = 1

    for pair in polymer:
        if pair[0] not in count: count[pair[0]] = 0
        count[pair[0]] += polymer[pair]

    values = [v for v in count.values()]

    return max(values) - min(values)

if __name__ == '__main__':
    filename = 'input.txt'
    if len(sys.argv) > 1:
        filename = sys.argv[1]

    file = open(filename)
    lines = [line.strip() for line in file]

    template = lines[0]

    rules = {}
    for line in lines[2:]:
        pair, ins = line.split(' -> ')
        rules[pair] = ins

    # Part One:
    # Apply 10 steps, what do you get if you take the quantity of the most common element and subtract the quantity of the least common element?
    polymer = get_polymer_from(template)

    for i in range(10):
        polymer = step(polymer, rules)

    print("Part One:", get_quantity_delta(template, polymer))

    # Part Two:
    # Apply 40 steps, what do you get if you take the quantity of the most common element and subtract the quantity of the least common element?
    polymer = get_polymer_from(template)

    for i in range(40):
        polymer = step(polymer, rules)

    print("Part Two:", get_quantity_delta(template, polymer))
