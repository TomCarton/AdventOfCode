#!/usr/local/bin/python3.9

# Advent of Code 2020
# Day 12

f = open('input.txt', 'r')
lines = [line.strip() for line in f]

def moveShip(direction, amount):
    global ship

    if direction == 'W':
        ship[0] -= amount
    elif direction == 'E':
        ship[0] += amount
    elif direction == 'N':
        ship[1] -= amount
    elif direction == 'S':
        ship[1] += amount

def moveWaypoint(direction, amount):
    global waypoint

    if direction == 'W':
        waypoint[0] -= amount
    elif direction == 'E':
        waypoint[0] += amount
    elif direction == 'N':
        waypoint[1] += amount
    elif direction == 'S':
        waypoint[1] -= amount

def rotateWaypoint(direction, angle):
    global waypoint

    angle = angle // 90

    if angle == 1:
        waypoint[0], waypoint[1] = waypoint[1], -waypoint[0]
    elif angle == 2:
        waypoint[0], waypoint[1] = -waypoint[0], -waypoint[1]
    elif angle == 3:
        waypoint[0], waypoint[1] = -waypoint[1], waypoint[0]

# Part One:
# What is the Manhattan distance between that location and the ship's starting position?

ship = [0, 0]
orient = 0

for line in lines:
    action = line[0]
    value = int(line.strip()[1:])
 
    dir = action
    if action == 'R':
        orient -= value
    elif action == 'L':
        orient += value
    else:
        if action == 'F':
            dir = "ENWS"[(orient % 360) // 90]
        moveShip(dir, value)

print("Part One:", abs(ship[0]) + abs(ship[1]))

# Part Two:
# What is the Manhattan distance between that location and the ship's starting position?

ship = [0, 0]
waypoint = [10, 1]

for line in lines:
    action = line[0]
    value = int(line.strip()[1:])

    dir = action

    if action == 'R':
        rotateWaypoint(action, value)
    elif action == 'L':
        rotateWaypoint(action, 360 - value)
    else:
        if action == 'F':
            ship[0] += waypoint[0] * value
            ship[1] += waypoint[1] * value
        else:
            moveWaypoint(dir, value)

print("Part Two:", abs(ship[0]) + abs(ship[1]))
