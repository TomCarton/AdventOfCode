#!/usr/bin/env python3

import sys
from itertools import combinations
from collections import defaultdict


input_filename = "input.txt"
if len(sys.argv) > 1 and sys.argv[1]:
    input_filename = sys.argv[1]

with open(input_filename) as file:
    connections = [line.strip().split('-') for line in file]

network = defaultdict(set)
for cnx1, cnx2 in connections:
    network[cnx1].add(cnx2)
    network[cnx2].add(cnx1)

# Part One:
#
p1 = 0

for node in network:
    connections = network[node]
    for n1, n2 in combinations(connections, 2):
        if n2 in network[n1]:
            if node.startswith('t') or n1.startswith('t') or n2.startswith('t'):
                p1 += 1

print("  Part One:", p1 // 3)

# Part Two:
#
max_set = []

for node in network:
    current_set = {node}

    candidates = network[node]
    for neighbor in candidates:
        if all(neighbor in network[n] for n in current_set):
            current_set.add(neighbor)

    if len(current_set) > len(max_set):
        max_set = list(current_set)

p2 = ",".join(sorted(max_set))

print("  Part Two:", p2)
