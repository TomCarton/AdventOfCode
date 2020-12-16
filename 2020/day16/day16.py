#!/usr/local/bin/python3.9

# Advent of Code 2020
# Day 16

def valuesForRange(str):
    low, high = str.split('-')
    return set(range(int(low), int(high) + 1))

# Part One:
# What is your ticket scanning error rate?

def scan(fields, tickets):
    validTickets = []
    errorRate = 0

    for ticket in tickets:
        for value in ticket:
            found = False
            for c in fields.values():
                for p in c:
                    if value in p:
                        found = True
                        break
                if found:
                    break
            else:
                errorRate += value
                break
        else:
            validTickets.append(ticket)

    return (validTickets, errorRate)

# Part Two:
# Look for the six fields on your ticket that start with the word departure

def determineDeparture(fields, tickets, myTicket):
    fieldOrder = [[] for _ in range(len(fields))]
    for fieldName, field in fields.items():
        for idx in range(len(fields)):
            for t in tickets:
                if t[idx] not in field[0] and t[idx] not in field[1]:
                    break
            else:
                fieldOrder[idx].append(fieldName)

    count = toRemove = 1
    while toRemove:
        toRemove = None
        for idx, field in enumerate(fieldOrder):
            if len(field) == 1:
                if field[0].startswith('departure'):
                    count *= myTicket[idx]
                toRemove = field[0]

        if toRemove:
            for field in fieldOrder:
                if toRemove in field:
                    field.remove(toRemove)

    return count

# Main
#

if __name__ == "__main__":
    f = open('input.txt', 'r')
    input = f.read().strip().split('\n\n')

    fields = {row.split(': ')[0]: list(map(valuesForRange, row.split(': ')[1].split(' or '))) for row in input[0].split('\n')}
    myTicket = [int(v) for v in input[1].split('\n')[1].split(',')]
    tickets = [list(map(int, t.split(','))) for t in input[2].split('\n')[1:]]

    scanResult = scan(fields, tickets)
    departureResult = determineDeparture(fields, scanResult[0], myTicket)

    print("Part One:", scanResult[1])
    print("Part Two:", departureResult)
