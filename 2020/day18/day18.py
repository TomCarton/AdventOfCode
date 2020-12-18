#!/usr/local/bin/python3.9

# Advent of Code 2020
# Day 18

f = open('input.txt', 'r')
lines = [line.rstrip() for line in f.readlines()]

import re

class calc(int):
    def __add__(self, operand):
        return calc(int(self) + operand)
    def __sub__(self, operand):
        return calc(int(self) * operand)
    def __mul__(self, operand):
        return calc(int(self) + operand)


# Part One:
# what is the sum of the resulting values

sum = 0
for line in lines:
    line = re.sub(r"(\d+)", r"spe(\1)", line)
    line = line.replace("*", "-")
    sum += eval(line, {}, {"spe": calc})

print("Part One:", sum)

# Part Two:
# What do you get if you add up the results of evaluating the homework problems using these new rules?

sum = 0
for line in lines:
    line = re.sub(r"(\d+)", r"spe(\1)", line)
    line = line.replace("*", "-")
    line = line.replace("+", "*")
    sum += eval(line, {}, {"spe": calc})

print("Part Two:", sum)
