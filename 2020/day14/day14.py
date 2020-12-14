#!/usr/local/bin/python3.9

# Advent of Code 2020
# Day 14

f = open('input.txt', 'r')
lines = [line.strip() for line in f]

# Part One:
# What is the sum of all values left in memory after it completes?
memory = dict()
mask = None

for instruction in lines:
    var, data = instruction.split(" = ")

    if var == "mask":
        mask = data
    elif var.startswith("mem"):
        address = var[4:-1]
        data = list(bin(int(data))[2:].zfill(36))

        for idx, bit in enumerate(mask):
            if bit != 'X':
                data[idx] = bit

        data = int("".join(data), 2)
        memory[address] = data

print("Part 1:", sum(memory.values()))

# Part Two:
# What is the sum of all values left in memory after it completes?
memory = dict()
mask = None

for instruction in lines:
    var, data = instruction.split(" = ")

    if var == "mask":
        mask = data
    elif var.startswith("mem"):
        address = var[4:-1]

        address = list(bin(int(address))[2:].zfill(36))
        for idx, bit in enumerate(mask):
            if bit == '1':
                address[idx] = bit

        n = mask.count('X')
        for bits in range(2**n):
            bits = bin(bits)[2:].zfill(n)

            newAddress = address[:]
            b = 0
            for i, c in enumerate(mask):
                if c == 'X':
                    newAddress[i] = bits[b]
                    b += 1

            newAddress = int("".join(newAddress), 2)
            memory[newAddress] = int(data)

print("Part 2:", sum(memory.values()))
