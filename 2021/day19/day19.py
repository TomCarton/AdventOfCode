#!/usr/bin/python3
import sys
from itertools import permutations
from collections import defaultdict

# # Advent of Code 2021
# Day 19

# [0, 1, 2] permutations
perm3 = []
for p in list(permutations([0, 1, 2])):
    perm3.append((p[0], p[1], p[2]))

def reorient(point, d):
    p = perm3[d >> 3]
    r = [point[p[0]], point[p[1]], point[p[2]]]

    if d & 1: r[0] = -r[0]
    if d & 2: r[1] = -r[1]
    if d & 4: r[2] = -r[2]

    return r

if __name__ == '__main__':
    filename = 'input.txt'
    if len(sys.argv) > 1:
            filename = sys.argv[1]

    file = open(filename)
    data = file.read().strip().split('\n\n')

    scanners = []
    for scan in data:
        beacons = []

        for line in scan.split('\n'):
            line = line.strip()

            if line.startswith('--'):
                continue

            x,y,z = [int(v) for v in line.split(',')]
            beacons.append((x, y, z))

        scanners.append(beacons)

    # Part One:
    # Assemble the full map of beacons. How many beacons are there?

    count = len(scanners)
    final = set(scanners[0])

    P = [None for _ in range(count)]
    P[0] = (0,0,0)

    potential = set([x for x in range(1, count)])
    correct = set([0])

    orientations = {}
    for i in range(count):
        for orient in range(48):
            orientations[(i, orient)] = [reorient(p, orient) for p in scanners[i]]

    while potential:
        found = None
        for b in potential:
            if found:
                continue

            for g in [0]:
                g_scan = [tuple([p[0] + P[g][0], p[1] + P[g][1], p[2] + P[g][2]]) for p in final]
                g_set = set(g_scan)

                for orient in range(48):
                    b_scan = orientations[(b, orient)]

                    mark = defaultdict(int)

                    for bi in range(len(scanners[b])):
                        for gi in range(len(g_scan)):
                            dx = -b_scan[bi][0] + g_scan[gi][0]
                            dy = -b_scan[bi][1] + g_scan[gi][1]
                            dz = -b_scan[bi][2] + g_scan[gi][2]
                            mark[(dx, dy, dz)] += 1

                    for (dx,dy,dz), val in mark.items():
                        if val >= 12:
                            P[b] = (dx, dy, dz)

                            for p in b_scan:
                                final.add(tuple([p[0] + dx, p[1] + dy, p[2] + dz]))

                            found = b

        correct.add(found)
        potential.remove(found)

    print("Part One:", len(final))

    # Part Two:
    # What is the largest Manhattan distance between any two scanners?
    largest = 0
    for p1 in P:
        for p2 in P:
            distance = sum([abs(p2[i] - p1[i]) for i in range(3)])
            largest = max(distance, largest)

    print("Part Two:", largest)
