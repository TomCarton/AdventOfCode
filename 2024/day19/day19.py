#!/usr/bin/env python3

import sys
from functools import lru_cache

def has(design):
    if design == "":
        return True
    
    for token in patterns:
        if design.startswith(token) and has(design[len(token):]):
            return True

    return False

@lru_cache(None)
def count_tokens_in_design(design):
    if design == "":
        return 1
    
    ways = 0
    for pattern in patterns:
        if design.startswith(pattern):
            ways += count_tokens_in_design(design[len(pattern):])
    
    return ways


input_filename = "input.txt"
if len(sys.argv) > 1 and sys.argv[1]:
    input_filename = sys.argv[1]

data = open(input_filename).read().strip()
patterns, designs = data.split('\n\n')

patterns = patterns.split(', ')
designs = designs.split('\n')

# Part One:
#
p1 = 0

for design in designs:
    if has(design):
        p1 += 1

print("  Part One:", p1)


# Part Two:
#
p2 = 0

for design in designs:
    p2 += count_tokens_in_design(design)

print("  Part Two:", p2)
