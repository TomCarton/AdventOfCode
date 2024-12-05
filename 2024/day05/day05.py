#!/usr/bin/env python3

import sys
from collections import defaultdict, deque

def build_graph(rules):
    graph = defaultdict(list)

    for rule in rules:
        x, y = map(int, rule.split("|"))

        graph[x].append(y)

    return graph


def is_valid_update(update, graph):
    subgraph = defaultdict(list)
    for x in update:
        subgraph[x] = [y for y in graph[x] if y in update]

    in_degree = {x: 0 for x in update}
    for x in subgraph:
        for y in subgraph[x]:
            in_degree[y] += 1

    queue = deque([x for x in update if in_degree[x] == 0])
    sorted_order = []
    while queue:
        node = queue.popleft()
        sorted_order.append(node)
        for neighbor in subgraph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Check if sorted_order matches the update
    return sorted_order == update


def reorder_update(update, graph):
    subgraph = defaultdict(list)
    for x in update:
        subgraph[x] = [y for y in graph[x] if y in update]

    in_degree = {x: 0 for x in update}
    for x in subgraph:
        for y in subgraph[x]:
            in_degree[y] += 1

    queue = deque([x for x in update if in_degree[x] == 0])
    sorted_order = []
    while queue:
        node = queue.popleft()
        sorted_order.append(node)
        for neighbor in subgraph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_order


input_filename = "input.txt"
if len(sys.argv) > 1 and sys.argv[1]:
    input_filename = sys.argv[1]

sections = open(input_filename).read().strip().split("\n\n")

rules = [line.strip() for line in sections[0].splitlines()]
updates = [list(map(int, line.strip().split(","))) for line in sections[1].splitlines()]

graph = build_graph(rules)

# Part One:
#
p1 = 0

valid_updates = []
for update in updates:
    if is_valid_update(update, graph):
        valid_updates.append(update)

middle_sum = 0
for update in valid_updates:
    middle_page = update[len(update) // 2]
    p1 += middle_page


print("  Part One:", p1)

# Part Two:
#
p2 = 0

valid_updates = []
invalid_updates = []
for update in updates:
    if is_valid_update(update, graph):
        valid_updates.append(update)
    else:
        invalid_updates.append(update)

for update in invalid_updates:
    reordered = reorder_update(update, graph)
    middle_page = reordered[len(reordered) // 2]
    p2 += middle_page

print("  Part Two:", p2)
