#!/usr/bin/python3

# # Advent of Code 2021
# Day 10

match = { '{': '}', '[': ']', '(': ')', '<': '>' }
corruption_points = { ')': 3, ']': 57, '}': 1197, '>': 25137 }
completion_points = { ')': 1, ']': 2, '}': 3, '>': 4 }

if __name__ == '__main__':
    file = open('input.txt')
    lines = [line.strip() for line in file]

    corruption_score = 0
    completion_scores = []

    for line in lines:
        to_close = []

        corrupted = False
        for c in line:
            if c in "({[<":
                to_close.append(c)
            else:
                if match[to_close[-1]] != c:
                    corrupted = True
                    corruption_score += corruption_points[c]
                    break
                else:
                    to_close.pop()

        # print("".join(to_close))

        if not corrupted:
            completion_score = 0
            for i, c in enumerate(to_close[::-1]):
                completion_score *= 5
                completion_score += completion_points[match[c]]
            completion_scores.append(completion_score)

    completion_scores.sort()

    # Part One:
    # What is the total syntax error score for those errors?
    print("Part One:", corruption_score)

    # Part Two:
    # Find the completion string for each incomplete line, score the completion strings, and sort the scores. What is the middle score?
    print("Part Two:", completion_scores[int((len(completion_scores) - 1) >> 1)])
