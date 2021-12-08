#!/usr/bin/python3
import itertools

# # Advent of Code 2021
# Day 08

mapping = {
    "abcdeg": 0,
    "ab": 1,
    "acdfg": 2,
    "abcdf": 3,
    "abef": 4,
    "bcdef": 5,
    "bcdefg": 6,
    "abd": 7,
    "abcdefg": 8,
    "abcdef": 9,
}

if __name__ == '__main__':
    file = open('input.txt')
    lines = [line.strip() for line in file]
    entries = [line.split(" | ") for line in lines]

    # Part One:
    # In the output values, how many times do digits 1, 4, 7, or 8 appear?

    output = [entry[1].split() for entry in entries]

    count = 0
    for i in output:
        for j in i:
            if len(j) in [2, 3, 4, 7]:
                count += 1

    print( "Part One:", count)

    # Part Two:
    # What do you get if you add up all of the output values?

    total = 0

    for entry in entries:
        signals, outputs = entry[0].split(), entry[1].split()
        for permutation in itertools.permutations("abcdefg"):
            scramble = { signals: outputs for signals, outputs in zip(permutation, "abcdefg") }
            scrambled_signals = ["".join(sorted(scramble[c] for c in signal)) for signal in signals]
            if all(scrambled_signal in mapping for scrambled_signal in scrambled_signals):
                scrambled_outputs = ["".join(sorted(scramble[c] for c in output)) for output in outputs]
                total += int("".join(str(mapping[x]) for x in scrambled_outputs))
                break

    print("Part Two:", total)
