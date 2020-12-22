#!/usr/local/bin/python3.9

# Advent of Code 2020
# Day 22

def readDecks():
    with open("input.txt", "r") as f:
        deck1, deck2 = f.read().strip().split('\n\n')
    return ([int(num) for num in deck1.split('\n')[1:]], [int(num) for num in deck2.split('\n')[1:]])

def computeScore(deck):
    return sum([deck[i] * (len(deck) - i) for i in range(len(deck))])

# Part One:
# What is the winning player's score?
def playGamePartOne(p1, p2):
    while p1 and p2:
        card1 = p1.pop(0)
        card2 = p2.pop(0)

        if card1 > card2:
            p1.append(card1)
            p1.append(card2)
        else:
            p2.append(card2)
            p2.append(card1)

    return p1 + p2

santa, crab = readDecks()
result = playGamePartOne(santa, crab)
print('Part One:', computeScore(result))

# Part Two:
# What is the winning player's score?
def recurse(p1, p2):
    prev = []
    while p1 and p2:
        state = [p1[:], p2[:]]
        if state in prev:
            return True
        prev.append(state)

        c1 = p1.pop(0)
        c2 = p2.pop(0)
        if c1 <= len(p1) and c2 <= len(p2):
            result = recurse(p1[:c1], p2[:c2])
        else:
            result = c1 > c2

        if result:
            p1.append(c1)
            p1.append(c2)
        else:
            p2.append(c2)
            p2.append(c1)

    return p1 > p2

def playGamePartTwo(p1, p2):
    prev = []
    while p1 and p2:
        state = [p1[:], p2[:]]
        if state in prev:
            break
        prev.append(state)

        c1 = p1.pop(0)
        c2 = p2.pop(0)
        if c1 <= len(p1) and c2 <= len(p2):
            result = recurse(p1[:c1], p2[:c2])
        else:
            result = c1 > c2

        if result:
            p1.append(c1)
            p1.append(c2)
        else:
            p2.append(c2)
            p2.append(c1)

    return p1 + p2

santa, crab = readDecks()
result = playGamePartTwo(santa, crab)
print('Part Two:', computeScore(result))
