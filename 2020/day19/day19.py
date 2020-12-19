#!/usr/local/bin/python3.9
import re, sys
sys.setrecursionlimit(2020)

# Advent of Code 2020
# Day 19

input = open('input.txt', 'rt').read()

rules, messages = input.split('\n\n')
rules = { int(index): rule for index, rule in [r.split(': ') for r in rules.splitlines()] }

messages = messages.splitlines()

def extract(index = 0, depth = 0):
    rule = rules[index]

    if rule.startswith('"'):
        return rule.replace('"', '')

    vars = []
    variants = rule.split(' | ')
    for v in variants:
        cats = []
        for a in v.split(' '):
            r = '' if depth > 500 else extract(int(a), depth + 1)
            cats.append(r)

        vars.append(''.join(cats))

    group = '|'.join(vars)

    return '(' + group + ')'

# Part One:
# How many messages completely match rule 0?

pattern = extract()
result = [message for message in messages if re.fullmatch(pattern, message)]

print("Part One:", len(result))

# Part Two:
# How many messages completely match rule 0? (with updated rule #8 and #11)

rules[8] = "42 | 42 8"
rules[11] = "42 31 | 42 11 31"

pattern = extract()
result = [message for message in messages if re.fullmatch(pattern, message)]

print("Part Two:", len(result))
