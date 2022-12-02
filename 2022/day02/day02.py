#!/usr/bin/python3
import sys
import os

# Advent of Code 2022
# Day 02

def main(filename):
    file = open(filename)
    inputs = file.readlines()

    # Part One:
    # What would your total score be if everything goes exactly according to your strategy guide?

    score = 0
    scoring = [
        [4, 8, 3],
        [1, 5, 9],
        [7, 2, 6],
    ]

    for line in inputs:
        round = line.strip().split(' ')

        first_hand = ord(round[0]) - ord('A')
        second_hand = ord(round[1]) - ord('X')

        score += scoring[first_hand][second_hand]

    print("Part One:", score)

    # Part Two:
    # Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?

    score = 0
    scoring = [
        [3, 4, 8],
        [1, 5, 9],
        [2, 6, 7],
    ]

    for line in inputs:
        round = line.strip().split(' ')

        first_hand = ord(round[0]) - ord('A')
        second_hand = ord(round[1]) - ord('X')

        score += scoring[first_hand][second_hand]

    print("Part Two:", score)

# Main
if __name__ == '__main__':
    path = os.path.dirname(os.path.join(os.getcwd(), sys.argv[0]).replace("/./", "/"))

    filename = os.path.join(path, 'input.txt')
    if len(sys.argv) > 1:
        filename = sys.argv[1]

    main(filename)
