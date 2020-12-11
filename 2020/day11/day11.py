#!/usr/local/bin/python3.9

import itertools

# Advent of Code 2020
# Day 11

surroundings = [(i, j) for i, j in itertools.product(range(-1, 2), repeat = 2) if (i != 0 or j != 0)]
# print(surroundings)

def countSeats(seats, row, col, visible):
    count = 0

    for i, j in surroundings:
        x = col + i
        y = row + j

        if visible:
            while 0 <= y < len(seats) and 0 <= x < len(seats[y]):
                if seats[y][x] == '.':
                    x += i
                    y += j
                elif seats[y][x] == "#":
                    count += 1
                    break
                else:
                    break
        else:
            if 0 <= row + j < len(seats) and 0 <= col + i < len(seats[row + j]):
                if seats[row + j][col + i] == "#":
                    count += 1

    return count

def compute(seats, tolerance, visible):
    prev = []

    while prev != seats:
        prev = seats[:]
        seats = []

        for row, y in enumerate(prev):
            line = ""
            
            for col, x in enumerate(y):
                neighbors = countSeats(prev, row, col, visible)
                
                if x == 'L':
                    line += '#' if neighbors == 0 else 'L'
                elif x == '#':
                    line += 'L' if neighbors >= tolerance else '#'
                else:
                    line += x
            
            seats.append(line)
    
    return list(itertools.chain(*seats)).count('#')

f = open('input.txt', 'r')
seats = f.read().splitlines()

# Part One:
# Four or more occupied seats for an occupied seat to become empty
# How many seats end up occupied?
result = compute(seats, 4, False)

print("Part One:", result)

# Part Two:
# Five or more visible occupied seats for an occupied seat to become empty
# How many seats end up occupied?
result = compute(seats, 5, True)

print("Part Two:", result)
