#!/usr/local/bin/python3.9
import itertools

# Advent of Code 2020
# Day 13

f = open('input.txt', 'r')
lines = [line.strip() for line in f]

timestamp = int(lines[0])
buses = lines[1].split(',')

# Part One:
#

nextBus = (-1, timestamp)
for bus in buses:
    if bus.isdigit():
        busId = int(bus)

        departure = busId - (timestamp % busId)
        if departure < nextBus[1]:
            nextBus = (busId, departure)

print(f'Part One: {nextBus[0] * nextBus[1]}')

# Part Two:
#

time = [int(bus) if bus != "x" else 1 for bus in buses]

# range = range(len(time))

# product = 1
# for index in range:
#     product *= time[index]

# result = 0
# for index in range:
#     t = time[index]
#     dt = product // t

#     x0, x1 = 0, 1
#     m, n = t, dt
#     while (n > 1):
#         x0, x1 = x1 - (n // m) * x0, x0
#         n, m = m, n % m

#     x = x1 if x1 > 0 else x1 + t
#     result += x * dt * -(index % t)

# print(f'Part Two: {result % product}')


sharedTimestamp, step = timestamp, 1
for i, b in [(i, b) for i, b in enumerate(time) if b != 'x']:
    for currentTimestamp in itertools.count(sharedTimestamp, step):
        if (currentTimestamp + i) % b == 0:
            sharedTimestamp, step = currentTimestamp, step * b
            break

print(f'Part Two:', sharedTimestamp)
