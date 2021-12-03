#!/usr/bin/python3

# # Advent of Code 2021
# Day 03

if __name__ == '__main__':

    file = open('input.txt')
    lines = [line.strip() for line in file]

    midCount = len(lines) // 2
    bitCount = len(lines[0])

    # Part One:
    # What is the power consumption of the submarine?

    count1 = [0] * bitCount
    for line in lines:
         for i, c in enumerate(line):
            if c == '1':
                count1[i] += 1

    gamma = 0
    pow = 2 ** (bitCount - 1)
    for i in range(bitCount):
        if count1[i] >= midCount:
            gamma += pow
        pow //= 2

    epsilon = ~gamma & 2 ** bitCount - 1

    print( "Part One: {:d}".format(gamma * epsilon) )

    # Part Two:
    # What is the life support rating of the submarine?

    i = 0
    numbers = set(lines)
    while len(numbers) > 1:
        count0 = 0
        count1 = 0

        for n in numbers:
            if n[i] == "0":
                count0 += 1
            elif n[i] == "1":
                count1 += 1

        for n in tuple(numbers):
            if n[i] == ("1" if count1 < count0 else "0"):
                numbers.remove(n)

        i += 1

    o = int(next(iter(numbers)), 2)

    i = 0
    numbers = set(lines)
    while len(numbers) > 1:
        count0 = 0
        count1 = 0

        for n in numbers:
            if n[i] == "0":
                count0 += 1
            elif n[i] == "1":
                count1 += 1

        for n in tuple(numbers):
            if n[i] == ("0" if count1 < count0 else "1"):
                numbers.remove(n)

        i += 1

    c = int(next(iter(numbers)), 2)
    print( "Part Two: {:d}".format(o * c) )
