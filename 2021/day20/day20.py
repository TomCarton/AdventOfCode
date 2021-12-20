#!/usr/bin/python3
import sys
import copy

# # Advent of Code 2021
# Day 20

SIZE = 1000

# Print iterations progress
# https://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()

if __name__ == '__main__':
    filename = 'input.txt'
    if len(sys.argv) > 1:
        filename = sys.argv[1]

    file = open(filename)
    lines = [line.strip() for line in file]

    algo = lines[0]
    image = lines[2:]

    m = [['.' for _ in range(SIZE)] for _ in range(SIZE)]

    r = len(image)
    c = len(image[0])

    # Part One:
    # How many pixels are lit in the resulting image?

    for j in range(r):
        for i in range(c):
            m[SIZE // 2 + j][SIZE // 2 + i] = image[j][i]

    for k in range(2):
        newm = copy.deepcopy(m)
        for i in range(len(m)):
            printProgressBar(k * len(m) + i, 2 * len(m), prefix = 'Part One:', length = 50)

            for j in range(len(m[i])):
                if i == 0 or i == len(m) - 1:
                    newm[i][j] = '#' if m[i][j] == '.' else '.'
                elif j == 0 or j == len(m[i]) - 1:
                    newm[i][j] = '#' if m[i][j] == '.' else '.'
                else:
                    current = m[i - 1][j - 1] + m[i - 1][j] + m [i - 1][j + 1] + m[i][j - 1] + m[i][j] + m[i][j + 1] + m[i + 1][j - 1] + m[i + 1][j] + m[i + 1][j + 1]
                    current = int(current.replace('.', '0').replace('#', '1'), 2)
                    newm[i][j] = algo[current]
        m = copy.deepcopy(newm)

    count = 0

    for i in m:
        count += i.count('#')

    print("Part One:", count, 60 * " ")

    # Part Two:
    # How many pixels are lit in the resulting image?

    for i in range(r):
        for j in range(c):
            m[SIZE // 2 + i][SIZE // 2 + j] = image[i][j]

    for it in range(50):
        printProgressBar(it, 50, prefix = 'Part Two:', length = 50)

        newm = copy.deepcopy(m)
        for i in range(len(m)):
            for j in range(len(m[i])):
                if i == 0 or i == len(m) - 1:
                    newm[i][j] = '#' if m[i][j] == '.' else '.'
                elif j == 0 or j == len(m[i]) - 1:
                    newm[i][j] = '#' if m[i][j] == '.' else '.'
                else:
                    current = m[i - 1][j - 1] + m[i - 1][j] + m [i - 1][j + 1] + m[i][j - 1] + m[i][j] + m[i][j + 1] + m[i + 1][j - 1] + m[i + 1][j] + m[i + 1][j + 1]
                    current = int(current.replace('.', '0').replace('#', '1'), 2)
                    newm[i][j] = algo[current]
        m = copy.deepcopy(newm)

    count = 0
    for i in m:
        count += i.count('#')

    print("Part Two:", count, 60 * " ")
