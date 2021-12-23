#!/usr/bin/python3
import sys
import time

# # Advent of Code 2021
# Day 23

lines = (*((*line,) for line in open("input.txt")),)
typeCost = {'A':1, 'B':10, 'C':100, 'D':1000}
rooms = {'A': 3, 'B':5, 'C':7, 'D':9}

cache = {}

def is_amphipod(data, x, y):
    val = data[y][x]
    return val if val in rooms.keys() else False

def is_correct_room(data, x, y):
    if not is_amphipod(data, x, y):
        return False

    if x == rooms[data[y][x]]:
        return True

    return False

def is_empty(data, x, y):
    return data[y][x] == '.'

def is_room_empty(data, x):
    for y in range(2, 2 + len(data) - 3):
        if not is_empty(data, x, y):
            return False

    return True

def has_room_available(data, x, y):
    amphipod = data[y][x]
    room = rooms[amphipod]

    if is_room_empty(data, room):
        return True

    for y in range(2, 2 + len(data) - 3):
        if not is_empty(data, room, y) and not is_correct_room(data, room, y):
            return False

    return True

def is_room_full(data, x):
    for y in range(2, 2 + len(data) - 3):
        if not is_correct_room(data, x, y):
            return False

    return True

def is_path_empty(data, x, targetX):
    while x != targetX:
        if x > targetX:
            x -= 1
        if x < targetX:
            x += 1

        if not is_empty(data, x, 1):
            return False

    return True

def is_blocking_room(data, x, y):
    for j in range(y+1, 2 + len(data) - 3):
        if is_amphipod(data, x, j) and not is_correct_room(data, x, j):
            return True
    return False

def is_blocked_in_room(data, x, y):
    if y < 3: return False
    return not is_empty(data, x, y-1)

def move_in_pos(data, room):
    for y in range(1 + len(data) - 3, 1, -1):
        if is_empty(data, room, y):
            return y

def move(data, x, y, i, j):
    newData = (*((*(((data[b][a], \
                      data[y][x])[a == i and b == j], \
                      data[j][i])[a == x and b == y] \
                    for a in range(len(data[b]))),) for b in range(len(data))),)
    return (newData, ((y - 1) + abs(x - i) + (j - 1)) * typeCost[data[y][x]])

def dump(data):
    print((len(data) + 1) * "\033[A")
    for l in data:
        print("".join(l[:-1:]))
    time.sleep(0.02)

def solve(data, display = False):
    cached = cache.get(data)
    if cached is not None:
        return cached

    if display:
        dump(data)

    if all([is_room_full(data, k) for k in [3, 5, 7, 9]]):
        return 0

    costs = []
    for y in range(1, len(data)):
        for x in range(1, len(data[y])):
            amphipod = is_amphipod(data, x, y)
            if amphipod and (not is_correct_room(data, x, y) or is_blocking_room(data, x, y)) and not is_blocked_in_room(data, x, y):
                room = rooms[amphipod]
                if has_room_available(data, x, y) and is_path_empty(data, x, room):
                    d, c = move(data, x, y, room, move_in_pos(data, room))

                    cost = solve(d, display)

                    if cost >= 0:
                        costs.append(c + cost)

                elif y > 1:
                    for i in tuple(i for i in range(1, len(data[0]) - 1) if i not in rooms.values()):
                        if is_path_empty(data, x, i):
                            d, c = move(data, x, y, i, 1)

                            cost = solve(d, display)

                            if cost >= 0:
                                costs.append(c + cost)

    result = -1
    if costs:
        result = min(costs)

    cache[data] = result
    return result

if __name__ == '__main__':
    filename = 'input.txt'
    if len(sys.argv) > 1:
        filename = sys.argv[1]

    file = open(filename)
    lines = (*((*line,) for line in file),)

    print(5 * "\n")

    # Part One:
    # What is the least energy required to organize the amphipods?
    dump(lines)
    min_cost = solve(lines, False)
    print("\nPart One:", min_cost, 8 * "\n")

    # Part Two:
    # Using the initial configuration from the full diagram, what is the least energy required to organize the amphipods?
    extended = (*lines[:3], (*"  #D#C#B#A# ",), (*"  #D#B#A#C# ",), *lines[3:],)
    dump(extended)

    min_cost = solve(extended, False)
    print("\nPart Two:", min_cost, "\n")
