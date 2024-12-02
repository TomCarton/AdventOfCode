#!/usr/bin/env python3

import sys

input_filename = "input.txt"
if len(sys.argv) > 1 and sys.argv[1]:
    input_filename = sys.argv[1]

data = open(input_filename).read().strip()
lines = data.splitlines()

reports = [list(map(int, line.split())) for line in lines]

# Part One:
#
p1 = 0

for report in reports:
    if report == sorted(report) or report == sorted(report, reverse=True):
        if all(abs(b - a) >= 1 and abs(b - a) <= 3 for a, b in zip(sorted(report), sorted(report)[1:])):
            p1 += 1

print("  Part One:", p1)

# Part Two:
#
p2 = 0

for report in reports:
    for i in range(len(report)):
        alt = report[:i] + report[i + 1:]
        if (alt == sorted(alt) or alt == sorted(alt, reverse=True)):
            if all(abs(b - a) >= 1 and abs(b - a) <= 3 for a, b in zip(sorted(alt), sorted(alt)[1:])):
                p2 += 1
                break

print("  Part Two:", p2)
