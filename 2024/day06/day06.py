#!/usr/bin/env python3

import sys

dirL = [[-1, 0], [0, 1], [1, 0], [0, -1]]


input_filename = "input.txt"
if len(sys.argv) > 1 and sys.argv[1]:
    input_filename = sys.argv[1]

lines = open(input_filename).read().splitlines()

data = [list(i) for i in lines if i != ""]
w, h = len(data[0]), len(data)

a, b = 0, 0
for i, v in enumerate(data):
    if "^" in v:
        a = i
        b = v.index("^")
        break

start_a, start_b = a, b
data[a][b] = "."


# Part One:
#
p1 = 0

dir = 0
visited = set()
while a in range(h) and b in range(w):
    if (a, b) not in visited:
        visited.add((a, b))

    if (dir == 0 and a == 0) or (dir == 1 and b == w - 1) or (dir == 2 and a == h-1) or (dir == 3 and b == 0):
        break

    if data[a+dirL[dir][0]][b+dirL[dir][1]] == "#":
        dir = (dir + 1) % 4
    else:
        a += dirL[dir][0]
        b += dirL[dir][1]

p1 = len(visited)

print("  Part One:", p1)

# Part Two:
#
p2 = 0

dir = 0
for i in range(h):
    for j in range(w):
        if data[i][j] == "#":
            continue

        data[i][j] = "#"
        a, b = start_a, start_b

        dir = 0
        visited = set()
        while a in range(h) and b in range(w):
            if (a, b, dir) not in visited:
                visited.add((a, b, dir))
            else:
                p2 += 1
                break

            if (dir == 0 and a == 0) or (dir == 1 and b == w - 1) or (dir == 2 and a == h - 1) or (dir == 3 and b == 0):
                break

            if data[a + dirL[dir][0]][b + dirL[dir][1]] == "#":
                dir = (dir + 1) % 4
            else:
                a += dirL[dir][0]
                b += dirL[dir][1]

        data[i][j] = "."

print("  Part Two:", p2)
