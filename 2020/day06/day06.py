#!/usr/local/bin/python3.9
from collections import Counter

# Advent of Code 2020
# Day 6

def getInput(path: str = './input.txt') -> str:
    with open(path) as f:
        return f.read()

def main(input: str):
    anyone = 0
    everyone = 0

    for group in input.split('\n\n'):
        personCount = group.count('\n') + 1
        answers = group.replace('\n', '')

        anyone += len(set(answers))
        everyone += sum(count == personCount for _, count in Counter(answers).items())

    # Part One:
    # count the number of questions to which anyone answered "yes"
    print('Part One:', anyone)

    # Part Two:
    # count the number of questions to which everyone answered "yes"
    print('Part Two:', everyone)


if __name__ == '__main__':
    main(getInput())
