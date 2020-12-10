#!/usr/local/bin/python3.9

# Advent of Code 2020
# Day 10

f = open('input.txt', 'r')
adapters = [0] + [int(line.strip()) for line in f]
adapters.sort()
size = len(adapters)

# Part One:
# What is the number of 1-jolt differences multiplied by the number of 3-jolt differences?
diff1 = 1
diff3 = 1
for i in range(1, size - 1):
    diff = adapters[i + 1] - adapters[i]
    if diff == 1:
        diff1 += 1
    elif diff == 3:
        diff3 += 1

print("Part One:", diff1 * diff3)

# Part Two:
# What is the total number of distinct ways you can arrange the adapters to connect the charging outlet to your device?
ways = [0] * size

ways[0] = 1
for i in range(1, size):
    for j in range(0, i):
        if adapters[i] - adapters[j] <= 3:
            ways[i] += ways[j]

print("Part Two:", ways[-1])
