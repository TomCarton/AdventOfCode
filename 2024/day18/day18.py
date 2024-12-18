#!/usr/bin/env python3

import sys
import heapq

def heuristic(x, y):
    return abs(x - end[0]) + abs(y - end[1])

def astar(memorySpace, start, end):
    gridSize = len(memorySpace)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # priority, steps, position
    pq = [(0 + heuristic(*start), 0, start)]

    visited = set()
    while pq:
        _, steps, (x, y) = heapq.heappop(pq)

        if (x, y) == end:
            return steps

        if (x, y) in visited:
            continue

        visited.add((x, y))

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < gridSize and 0 <= ny < gridSize and not memorySpace[ny][nx] and (nx, ny) not in visited:
                heapq.heappush(pq, (steps + 1 + heuristic(nx, ny), steps + 1, (nx, ny)))

    return -1

input_filename = "input.txt"
if len(sys.argv) > 1 and sys.argv[1]:
    input_filename = sys.argv[1]

data = open(input_filename).read().strip()

lines = data.splitlines()
corrupted = [tuple(map(int, line.strip().split(','))) for line in lines]

gridSize = 71
start = (0, 0)
end = (gridSize - 1, gridSize - 1)

# Part One:
#

memorySpace = [[False] * gridSize for _ in range(gridSize)]

for x, y in corrupted[:1024]:
    if 0 <= x < gridSize and 0 <= y < gridSize:
        memorySpace[y][x] = True

print("  Part One:", astar(memorySpace, start, end))

# Part Two:
#

memorySpace = [[False] * gridSize for _ in range(gridSize)]

blockingByte = None
for idx, (x, y) in enumerate(corrupted):
    if 0 <= x < gridSize and 0 <= y < gridSize:
        memorySpace[y][x] = True

        if astar(memorySpace, start, end) == -1:
            blockingByte = (x, y)
            break

if blockingByte:
    print("  Part Two:", f"{blockingByte[0]}, {blockingByte[1]}")
