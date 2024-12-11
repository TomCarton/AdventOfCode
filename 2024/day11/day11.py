#!/usr/bin/env python3

import sys
from functools import cache

@cache
def arrangeStones(stone, blinks):
    if blinks > 0:
        blinks -= 1

        if stone == 0:
            return arrangeStones(1, blinks)
        
        strStone = str(stone)
        if len(strStone) & 1 == 0:
            half = len(strStone) // 2
            left = int(strStone[:half])
            right = int(strStone[half:])
            return arrangeStones(left, blinks) + arrangeStones(right, blinks)
        
        return arrangeStones(stone * 2024, blinks)

    return 1

input_filename = "input.txt"
if len(sys.argv) > 1 and sys.argv[1]:
    input_filename = sys.argv[1]

data = open(input_filename).read().splitlines()[0]
stones = list(map(int, data.split(' ')))

# Part One:
#
p1 = 0

for stone in stones:
    p1 += arrangeStones(stone, 25)

print("  Part One:", p1)

# Part Two:
#
p2 = 0

for stone in stones:
    p2 += arrangeStones(stone, 75)

print("  Part Two:", p2)
