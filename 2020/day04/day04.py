#!/usr/bin/python3

# Advent of Code 2020
# Day 04

import re

def ints(line):
    pattern = re.compile(r'-?\d+')
    return [int(val) for val in re.findall(pattern, line) if val]

# -- check passport --
def check(passport):
    required = { 'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid' }

    fields = set()
    valid = True

    for line in passport:
        for pair in line:
            k, v = list(pair.split(':'))
            fields.add(k)

            eval = {
                'byr': lambda v: (len(v) == 4 and 1920 <= int(v) <= 2002),
                'iyr': lambda v: (len(v) == 4 and 2010 <= int(v) <= 2020),
                'eyr': lambda v: (len(v) == 4 and 2020 <= int(v) <= 2030),

                'hcl': lambda v: (len(v) == 7 and v[0] == '#' and all(c in '0123456789abcdef' for c in v[1:])),
                'pid': lambda v: (len(v) == 9 and all(c in '0123456789' for c in v)),
                'ecl': lambda v: (v in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']),
            }

            if k == 'hgt':
                nums = ints(v)

                cm = len(v) > 1 and v[-2:] == 'cm'
                if cm and not 150 <= nums[0] <= 193:
                    valid = False

                inch = len(v) > 1 and v[-2:] == 'in'
                if inch and not 59 <= nums[0] <= 76:
                    valid = False

                if not (cm or inch):
                    valid = False
            elif k != 'cid':
                valid = valid and eval[k](v)

    return len(fields & required) == len(required), valid

# -- Main --
if __name__ == '__main__':
    passports = []
    passport = []

    with open('input.txt') as f:
        for line in f.readlines():
            if not line.strip():
                passports.append(passport)
                passport = []
            else:
                passport.append(line.split())

    if passport:
        passports.append(passport)

    passportCount = 0
    validCount = 0
    for passport in passports:
        present, valid = check(passport)

        if present:
            passportCount += 1
            if valid:
                validCount += 1

    # Part One:
    # Count the number of valid passports - those that have all required fields.

    print("Part One:", passportCount)

    # Part Two:
    # Count the passports where all required fields are both present and valid

    print("Part Two:", validCount)
