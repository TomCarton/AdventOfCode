#!/usr/bin/python3
import itertools as itt

# Advent of Code 2021
# Day 01

file = open('input.txt')
heights = [int(line.strip()) for line in file]

# Part One:
# How many measurements are larger than the previous measurement?

count = 0
for i in range(1, len(heights)):
    if heights[i] > heights[i - 1]:
        count += 1

print( "Part One: {:d}".format(count) )

# Part Two:
# How many sums are larger than the previous sum?

count = 0
priorWindow = heights[0] + heights[1] + heights[2]
for i in range(3, len(heights)):
    slidingWindow = heights[i - 2] + heights[i - 1] + heights[i]
    if slidingWindow > priorWindow:
        count += 1
    priorWindow = slidingWindow

print( "Part Two: {:d}".format(count) )
