#!/usr/bin/python3
import sys
import os

# Advent of Code 2022
# Day 17

rocks = [((0, 0), (1, 0), (2, 0), (3, 0)),
         ((1, 0), (0, 1), (1, 1), (2, 1), (1, 2)),
         ((0, 0), (1, 0), (2, 0), (2, 1), (2, 2)),
         ((0, 0), (0, 1), (0, 2), (0, 3)),
         ((0, 0), (1, 0), (0, 1), (1, 1))]

def drop_rocks(pattern, reps):
    pattern_index = 0
    rockPos = 0

    currPos = (2, 3)

    chamber = set()
    size = 7
    currMax = -1

    y_ups = dict()
    y_down = dict()

    additional = 0
    seen = dict()

    dropped = 0
    while dropped < reps:
        while True:
            rock = rocks[rockPos]
            posPos = currPos

            if pattern[pattern_index] == '<':
                posPos = (posPos[0] - 1, posPos[1])
            elif pattern[pattern_index] == '>':
                posPos = (posPos[0] + 1, posPos[1])

            pattern_index = (pattern_index + 1) % len(pattern)
            if any([coord_x + posPos[0] < 0 or coord_x + posPos[0] >= size or (coord_x + posPos[0], coord_y + posPos[1]) in chamber for coord_x, coord_y in rock]):
                posPos = currPos

            posPos = (posPos[0], posPos[1] - 1)
            if posPos[1] < 0 or any([(coord_x + posPos[0], coord_y + posPos[1]) in chamber for coord_x, coord_y in rock]):
                dropped += 1

                for coord_x, coord_y in rock:
                    chamber.add((coord_x + posPos[0], coord_y + posPos[1] + 1))

                    if coord_y + posPos[1] + 1 > currMax:
                        currMax = coord_y + posPos[1] + 1
                    if y_down.get(coord_x + posPos[0], -1) < coord_y + posPos[1] + 1:
                        y_down[coord_x + posPos[0]] = coord_y + posPos[1] + 1

                tops = tuple([y_down.get(i, -1) - currMax for i in range(7)])
                rockPos = (rockPos + 1) % len(rocks)

                currPos = (2, currMax + 4)
                if (tops, pattern_index, rockPos) in seen:
                    oldrocks, oldmax = seen[(tops, pattern_index, rockPos)]
                    repeat = (reps - dropped) // (dropped - oldrocks)
                    dropped += repeat * (dropped - oldrocks)
                    additional += repeat * (currMax - oldmax)
                    seen = dict()

                seen[(tops, pattern_index, rockPos)] = (dropped, currMax)
                break
            else:
                currPos = posPos

    return(currMax + 1 + additional)

def main(filename):
    file = open(filename)
    pattern = file.readline().strip()
    file.close()


    # Part One:
    # How many units tall will the tower of rocks be after 2022 rocks have stopped falling?
    result = drop_rocks(pattern, 2022)
    print("Part One:", result)

    # Part Two:
    # How tall will the tower be after 1000000000000 rocks have stopped?

    result = drop_rocks(pattern, 1_000_000_000_000)
    print("Part Two:", result)

# Main
if __name__ == '__main__':
    path = os.path.dirname(os.path.join(os.getcwd(), sys.argv[0]).replace("/./", "/"))

    filename = os.path.join(path, 'input.txt')
    if len(sys.argv) > 1:
        filename = sys.argv[1]

    main(filename)
