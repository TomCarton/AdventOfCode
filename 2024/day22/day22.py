#!/usr/bin/env python3

import sys
from collections import defaultdict
import re


input_filename = "input.txt"
if len(sys.argv) > 1 and sys.argv[1]:
    input_filename = sys.argv[1]

data = open(input_filename).read().strip()
lines = data.splitlines()

secrets = [int(line) for line in lines]


# Part One:
#
p1 = 0
for secret in secrets:
    for i in range(2000):
        secret = (secret ^ (secret << 6)) & 16777215
        secret = (secret ^ (secret >> 5)) & 16777215
        secret = (secret ^ (secret << 11)) & 16777215
    p1 += secret

print("  Part One:", p1)

# Part Two:
#
p2 = 0

subs = defaultdict(int)
for secret in secrets:
    patterns = []

    previous_price = secret % 10
    for i in range(2000):
        secret = (secret ^ (secret << 6)) & 16777215
        secret = (secret ^ (secret >> 5)) & 16777215
        secret = (secret ^ (secret << 11)) & 16777215

        tmp = secret % 10
        patterns.append((tmp - previous_price, tmp))
        previous_price = tmp

    seen = set()
    for i in range(len(patterns) - 4):
        pattern = tuple(x[0] for x in patterns[i : i + 4])
        value = patterns[i + 3][1]

        if pattern not in seen:
            seen.add(pattern)
            subs[pattern] += value

p2 = max(subs.values())

print("  Part Two:", p2)
