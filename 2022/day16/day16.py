#!/usr/bin/python3
import sys
import os
import re

# Advent of Code 2022
# Day 16

def read_valves(lines):
    # Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
    valves = {}

    for line in lines:
        line = line.strip()
        valve = line[6:8]
        flow, next_valves = line.split(";")

        _, rate = flow.split("=")
        rate = int(rate)

        next_valves = next_valves.split(",")
        next_valves[0] = next_valves[0][-2:]
        next_valves = [nv.strip() for nv in next_valves]

        valves[valve] = (rate, next_valves)

    return valves

def compute_distances(valves):
    distance = {}
    for va in valves:
        for vb in valves:
            if va == vb:
                distance[(va, vb)] = 0
            else:
                distance[(va, vb)] = sys.maxsize

    for i in range(len(valves)):
        for va in valves:
            for vb in valves:
                for vd in valves[vb][1]:
                    distance[(va, vd)] = min(distance[(va, vd)], distance[(va, vb)] + 1)

    return distance

def accumulate_pressure(remaining_days, cur, pressure, progress):
    global valves, distance, actives

    if remaining_days <= 1:
        return -1

    cv = valves[cur]

    if cv[0] > 0:
        remaining_days -= 1
        pressure += remaining_days * cv[0]
    result = pressure

    for i in actives:
        if i not in progress:
            progress.add(i)
            r = remaining_days - distance[(cur, i)]
            result = max(accumulate_pressure(r, i, pressure, progress), result)
            progress.remove(i)

    return result

def main(filename):
    global valves, distance, actives

    file = open(filename)
    lines = file.readlines()
    file.close()

    valves = read_valves(lines)
    distance = compute_distances(valves)

    actives = []
    for valve in valves:
        if valves[valve][0] > 0:
            actives.append(valve)

    # Part One:
    # Work out the steps to release the most pressure in 30 minutes. What is the most pressure you can release?

    result = accumulate_pressure(30, "AA", 0, set())
    print("Part One:", result)

    # Part Two:
    # With you and an elephant working together for 26 minutes, what is the most pressure you could release?

    print("Part Two:", result)


# Main
if __name__ == '__main__':
    path = os.path.dirname(os.path.join(os.getcwd(), sys.argv[0]).replace("/./", "/"))

    filename = os.path.join(path, 'input.txt')
    if len(sys.argv) > 1:
        filename = sys.argv[1]

    main(filename)
