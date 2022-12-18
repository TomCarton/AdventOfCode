#!/usr/bin/python3
import sys
import os

from collections import deque

# Advent of Code 2022
# Day 18

cube_faces = [(-1, 0, 0), (1, 0, 0), 
              (0, -1, 0), (0, 1, 0), 
              (0, 0, -1), (0, 0, 1)]

def get_cubes(lines):
    cubes = set()

    for line in lines:
        x, y, z = map(int, line.split(","))
        cubes.add((x, y, z))

    return cubes

def get_inverse(cubes):
    inverse = set()

    for x in range(max(x for x, y, z in cubes) + 1):
        for y in range(max(y for x, y, z in cubes) + 1):
            for z in range(max(z for x, y, z in cubes) + 1):
                if (x, y, z) not in cubes:
                    inverse.add((x, y, z))

    return inverse

def flood_fill_erode(cubes, initial_cube):
    queue = deque()

    queue.append(initial_cube)
    while len(queue) > 0:
        cube = queue.popleft()

        if cube in cubes:
            cubes.remove(cube)

            for dx, dy, dz in cube_faces:
                next_cube = (cube[0] + dx, cube[1] + dy, cube[2] + dz)
                if next_cube in cubes:
                    queue.append(next_cube)

def get_surface(cubes):
    count = 0

    for x, y, z in cubes:
        faces = 6

        for dx, dy, dz in cube_faces:
            if (x + dx, y + dy, z + dz) in cubes:
                faces -= 1

        count += faces

    return count

def main(filename):
    file = open(filename)
    lines = file.readlines()
    file.close()

    # Part One:
    # What is the surface area of your scanned lava droplet?
    cubes = get_cubes(lines)

    faces = get_surface(cubes)

    print("Part One:", faces)

    # Part Two:
    # What is the exterior surface area of your scanned lava droplet?
    cubes = get_cubes(lines)

    not_cubes = get_inverse(cubes)
    flood_fill_erode(not_cubes, (0, 0, 0))

    surface = get_surface(cubes) - get_surface(not_cubes)

    print("Part Two:", surface)

# Main
if __name__ == '__main__':
    path = os.path.dirname(os.path.join(os.getcwd(), sys.argv[0]).replace("/./", "/"))

    filename = os.path.join(path, 'input.txt')
    if len(sys.argv) > 1:
        filename = sys.argv[1]

    main(filename)
