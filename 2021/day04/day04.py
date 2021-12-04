#!/usr/bin/python3

# # # Advent of Code 2021
# # Day 04

def convert_to_grid(lines):
    grid = []
    for line in lines:
        l = []
        for c in line:
            if c.isnumeric():
                try:
                    val = int(c)
                except:
                    val = float(c)
            else:
                val = c
            l.append(val)
        grid.append(l)

    return grid

def is_bingo(board, row, col):
    val = 0
    for j in range(5):
        val += board[j][col]
    if val == 5:
        return True

    val = 0
    for i in range(5):
        val += board[row][i]
    if val == 5:
        return True

    return False

if __name__ == '__main__':
    file = open('input.txt')
    lines = [line.strip() for line in file]

    nums = [int(x) for x in lines[0].split(',')]

    new_lines = []
    for line in lines[2:]:
        if len(line) > 1:
            ls = line.split()
            new_lines.append(ls)
    lines = new_lines


    boards = []
    board_check = []
    i = 0
    while i < len(lines):
        boards.append(convert_to_grid(lines[i:i + 5]))
        new_board = [[0] * 5 for _ in range(5)]
        board_check.append(new_board)
        i += 5

    # Part One:
    # Figure out which board will win first. What will your final score be if you choose that board?

    last_winner = -1
    win_num = -1
    win_num_id = -1

    won = set()
    for idx, x in enumerate(nums):
        for i in range(len(boards)):
            for j in range(len(boards[i])):
                for k in range(len(boards[i][j])):
                    if boards[i][j][k] == x:
                        board_check[i][j][k] = 1

                        if is_bingo(board_check[i], j, k):
                            if last_winner == -1:
                                unmark = 0
                                for i2 in range(len(boards[i])):
                                    for j2 in range(len(boards[i][i2])):
                                        if board_check[i][i2][j2] == 0:
                                            unmark += boards[i][i2][j2]

                                print( "Part One:", unmark * x)

                            if i not in won:
                                won.add(i)

                                last_winner = i

                                win_num = x
                                win_num_id = idx

    # Part Two:
    # Figure out which board will win last. Once it wins, what would its final score be?

    for i in range(len(board_check)):
        board_check[i] = [[0] * 5 for _ in range(5)]

    for idx in range(win_num_id + 1):
        x = nums[idx]
        for i in range(len(boards)):
            for j in range(len(boards[i])):
                for k in range(len(boards[i][j])):
                    if boards[i][j][k] == x:
                        board_check[i][j][k] = 1

    unmark = 0
    for i2 in range(len(boards[last_winner])):
        for j2 in range(len(boards[last_winner][i2])):
            if board_check[last_winner][i2][j2] == 0:
                unmark += boards[last_winner][i2][j2]
    print("Part Two:", unmark * win_num)


