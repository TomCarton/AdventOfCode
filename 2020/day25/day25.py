#!/usr/local/bin/python3.9

# Advent of Code 2020
# Day 25

f = open('input.txt', 'r')

pkCard = int(f.readline())
pkDoor = int(f.readline())

mod = 20201227

# Last Puzzle:
#

x = 1
for i in range(1, mod):
    x = (x * 7) % mod
    if x == pkCard:
        loop1 = i
    if x == pkDoor:
        loop2 = i

hsDoor = pow(pkCard, loop2, mod)
hsCard = pow(pkDoor, loop1, mod)

if hsCard != hsDoor:
    print("!error: handshakes should match!")

print("Last Puzzle:", hsCard)
