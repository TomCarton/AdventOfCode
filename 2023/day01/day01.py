#!/usr/bin/env python3

import sys

input_filename = "input.txt"
if len(sys.argv) > 1 and sys.argv[1]:
    input_filename = sys.argv[1]

data = open(input_filename).read().strip()
lines = data.splitlines()

# What is the sum of all of the calibration values?

p1, p2 = 0, 0
for line in lines:
    np1, np2 = "", ""
    for i, c in enumerate(line):
        if c.isdigit():
            np1 += c
            np2 += c
        else:
            for n, num in enumerate(['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
                if line[i:].startswith(num):
                    np2 += str(n)

    p1 += int(np1[0] + np1[-1])
    p2 += int(np2[0] + np2[-1])

# Part One:
#
print("  Part One:", p1)

# Part Two:
# 
print("  Part Two:", p2)
