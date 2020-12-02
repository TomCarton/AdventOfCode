#!/usr/bin/python3

# # Advent of Code 2020
# Day 02

f = open('input.txt', 'r')
lines = [line.strip() for line in f]

# Part One:
# How many passwords are valid according to their policies?

valid = 0
for line in lines:
    element = line.split()
    minmax = element[0].split('-')
    count = element[2].count(element[1][0])
    if (count >= int(minmax[0]) and count <= int(minmax[1])):
        valid += 1

print("Part One:", valid)

# Part Two:
# How many passwords are valid according to the new interpretation of the policies?

valid = 0
for line in lines:
    element = line.split()
    index = element[0].split('-')
    letter = element[1][0]
    password = element[2] 
    valid += (password[int(index[0]) - 1] == letter) ^ (password[int(index[1]) - 1] == letter)

print("Part Two:", valid)
