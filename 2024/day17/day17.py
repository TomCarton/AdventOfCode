#!/usr/bin/env python3

import sys
import re

def dump(program):
    pc = 0
    while pc < len(program):
        [ins, op] = program[pc:(pc + 2)]

        match ins:
            case 0: # adv
                print("adv\tA // (2 ^ combo)")
            case 1: # bxl
                print("bxl\tB ^= op")
            case 2: # bst
                print("bst\tB = (combo % 8)")
            case 4: # bxc
                print("bxc\tB ^= C")
            case 5: # out
                print("out")
            case 6: # bdv
                print("bdv\tB = A // (2 ^ combo)")
            case 7: # cdv
                print("cdv\tC = A // (2 ^ combo)")

        pc += 2

def run(program, registers):
    output = []

    pc = 0
    while pc < len(program):
        [ins, op] = program[pc:(pc + 2)]

        combo = op if op <= 3 else registers[op - 4]

        match ins:
            case 0: # adv
                registers[0] = registers[0] // (2 ** combo)
            case 1: # bxl
                registers[1] ^= op
            case 2: # bst
                registers[1] = (combo % 8)
            case 3: # jnz
                if registers[0]:
                    pc = op - 2
            case 4: # bxc
                registers[1] ^= registers[2]
            case 5: # out
                output.append(combo % 8)
            case 6: # bdv
                registers[1] = registers[0] // (2**combo)
            case 7: # cdv
                registers[2] = registers[0] // (2**combo)

        pc += 2

    return output


input_filename = "input.txt"
if len(sys.argv) > 1 and sys.argv[1]:
    input_filename = sys.argv[1]

data = open(input_filename).read().strip()

register, program = data.split('\n\n')

registers = list(int(r[12:]) for r in register.splitlines())
program = list([int(i) for i in program[9:].split(',')])
#dump(program)

# Part One:
#

output = run(program, registers)
print("  Part One:", ','.join([str(i) for i in output]))


# Part Two:
#

check = { 0 }
for n in range(len(program)):
    possibles = set()

    for j in check:
        for registerA in range(8 * j, 8 * j + 8):
            output = run(program, [registerA] + registers[1:3])

            if output == program[-(n + 1):]:
                possibles.add(registerA)

    check = possibles

print("  Part Two:", min(check))
