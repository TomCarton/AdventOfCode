#!/usr/local/bin/python3.9

# Advent of Code 2020
# Day 15

def performMemoryRounds(startingNumbers, count):
    previously = {}
    startingNumbersCount = len(startingNumbers)

    for i in range(count - 1):
        if i < startingNumbersCount:
            previously[startingNumbers[i]], spoken = i, 0
        elif spoken not in previously:
            previously[spoken], spoken = i, 0
        else:
            previously[spoken], spoken = i, i - previously[spoken]

    return spoken

# Start

f = open('input.txt', 'r')
lines = [line.strip() for line in f]

input = [int(v) for v in lines[0].split(',')]

# Part One:
# Given your starting numbers, what will be the 2020th number spoken?

print("Part One:", performMemoryRounds(input, 2020))

# Part Two:
# Given your starting numbers, what will be the 30000000th number spoken?

print("Part Two:", performMemoryRounds(input, 30000000))
