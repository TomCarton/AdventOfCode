#!/usr/local/bin/python3.9

# Advent of Code 2020
# Day 08

instructions = []
with open('input.txt') as f:
    for line in f:
        operation, argument = line.strip().split(' ')

        argument = int(argument)
        instructions.append((operation, argument))

def execute(instructions):
    acc = 0
    pc = 0

    executed = len(instructions) * [False]
    while True:
        try:
            if executed[pc]:
                return False, acc
        except IndexError:
            return True, acc

        operation, argument = instructions[pc]
        executed[pc] = True

        if operation == 'jmp':
            pc += argument - 1
        elif operation == 'acc':
            acc += argument

        pc += 1


# Part One:
# Immediately before any instruction is executed a second time, what value is in the accumulator?

result, acc = execute(instructions)
print('Part One:', acc)

# Part Two:
# Fix the program so that it terminates normally. What is the value of the accumulator after the program terminates?

for pc, (operation, argument) in enumerate(instructions):
    if operation in ['nop', 'jmp']:
        modInstructions = list(instructions)
        modInstructions[pc] = ({'jmp': 'nop', 'nop': 'jmp'}[operation], argument)

        result, acc = execute(modInstructions)
        if result:
            break

print('Part Two:', acc)
