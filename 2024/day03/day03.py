#!/usr/bin/env python3

import sys
import re

input_filename = "input.txt"
if len(sys.argv) > 1 and sys.argv[1]:
    input_filename = sys.argv[1]

data = open(input_filename).read().strip()

# Part One:
#
pattern_mulus = r"mul\((\d{1,3}),(\d{1,3})\)"
mulus = re.findall(pattern_mulus, data)

mulu_numbers = [(int(num1), int(num2)) for num1, num2 in mulus]

p1 = 0
for numbers in mulu_numbers:
    p1 += numbers[0] * numbers[1]

print("  Part One:", p1)

# Part Two:
#
pattern_dont = r"don't\(\)"
pattern_do = r"do\(\)"

patterns = rf"{pattern_mulus}|{pattern_dont}|{pattern_do}"
ordered_matches = re.finditer(patterns, data)

count = 0
result_with_order = []
for match in ordered_matches:
    print(match.group(0))
    if match.group(1): 
        result_with_order.append(["mul", int(match.group(1)), int(match.group(2))])
    elif "don't()" in match.group(0):
        result_with_order.append("don't()")
    elif "do()" in match.group(0):
        result_with_order.append("do()")
    
    if ++count < 3:
        continue

    exit()

p2 = 0
enabled = True
for x in result_with_order:
    if x == "don't()":
        enabled = False
    elif x == "do()":
        enabled = True
    elif enabled:
        if type(x) == list:
            p2 += x[1] * x[2]

print("  Part Two:", p2)
