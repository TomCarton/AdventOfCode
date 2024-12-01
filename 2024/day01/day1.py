#!/usr/bin/env python3

import sys
# from collections import defaultdict

input_filename = "input.txt"
if len(sys.argv) > 1 and sys.argv[1]:
    input_filename = sys.argv[1]

data = open(input_filename).read().strip()
lines = data.splitlines()

left = []
right = []
for line in lines:
    vals = [int(x) for x in line.split()]

    left.append(vals[0])
    right.append(vals[1])

# Part One:
#
p1 = 0
for l,r in zip(sorted(left), sorted(right)):
    diff = abs(l - r)
    p1 += diff
print("  Part One:", p1)

# Part Two:
#
p2 = 0
for l, r in zip(left, right):
    count = right.count(l)
    p2 += l * count

print("  Part Two:", p2)
