#!/usr/bin/python3

# # Advent of Code 2020
# Day 01

f = open('input.txt', 'r')
lines = [int(line.strip()) for line in f]

# Part One:
# Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

found = False
for i in range(0, len(lines)):
    for j in range(i + 1, len(lines)):
        if lines[i] + lines[j] == 2020:
            found = True
        if found: break
    if found: break
if found:
    print( "Part One: {:d}".format(lines[i] * lines[j]) )

# Part Two:
# They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

found = False
for i in range(0, len(lines)):
    for j in range(i+1, len(lines)):
        for k in range(i+2, len(lines)):
            if lines[i] + lines[j] + lines[k] == 2020:
                found = True
                break
        if found: break
    if found: break
if found:
    print( "Part Two: {:d}".format(lines[i] * lines[j] * lines[k]) )
