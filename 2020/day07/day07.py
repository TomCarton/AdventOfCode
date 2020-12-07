#!/usr/local/bin/python3.9

# Advent of Code 2020
# Day 07

def parseContent(content):
    content = content.strip()
    content = content.strip("s.")[:-len(" bag")]
    content = content.split(" ", 1)
    content[0] = int(content[0])
    return content

rules = {}
with open('input.txt', "r") as f:
    for line in f:
        container, contents = line.split("bags", 1)

        container = container.strip()
        rules[container] = []

        contents = contents.strip()[len("contain "):]
        if not contents.startswith("no"):
            rules[container] = [parseContent(content) for content in contents.split(",")]        


# Part One:
# How many bag colors can eventually contain at least one shiny gold bag?

canContain = set()
while True:
    found = False
    for container, contents in rules.items():
        if container in canContain:
            continue

        allcontents = [item[1] for item in contents]
        if "shiny gold" in allcontents:
            found = True
 
            canContain.add(container)

        for item in allcontents:
            if item in canContain:
                found = True
 
                canContain.add(container)

    if not found:
        break

print('Part One:', len(canContain))


# Part Two:
# How many individual bags are required inside your single shiny gold bag?

def countBagsInside(container):
    count = 0

    for item in rules[container]:
        count += item[0] * (countBagsInside(item[1]) + 1)

    return count

print('Part Two:', countBagsInside("shiny gold"))
