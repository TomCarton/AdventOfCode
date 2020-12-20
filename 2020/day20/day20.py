#!/usr/local/bin/python3.9
import sys

# Advent of Code 2020
# Day 20

monsterCoords = [(0, 1), (1, 2), (4, 2), (5, 1), (6, 1), (7, 2), (10, 2), (11, 1), (12, 1), (13, 2), (16, 2), (17, 1), (18, 0), (18, 1), (19, 1)]
monsterWidth, monsterHeight = max(x for x, y in monsterCoords) + 1, max(y for x, y in monsterCoords) + 1

seaMonsters = set()

tiles, quadrans, side = {}, {}, 0

images = []
habitat = []

def readTiles(data):
    global tiles

    index = 0

    for line in data:
        if line == '\n':
            continue
        elif line.startswith('Tile'):
            index = int(line.replace('Tile', '').replace(':\n', ''))
        else:
            tiles.setdefault(index, []).append(line.strip())

    for index, tile in tiles.items():
        for j in range(8):
            quadrans[(index, j)] = tile
            if j & 1:
                tile = [''.join(col) for col in zip(*tile)]
            else:
                tile = [''.join(reversed(row)) for row in tile]

def addMonsters(habitat, monsters):
    for x, y in monsters:
        lst = list(habitat[y])
        lst[x] = 'O'
        habitat[y] = ''.join(lst)

def dumpHabitat(habitat):
    print(f"┌{'-' * (len(habitat[0]) + 2)}┐")
    for line in habitat:
        print('|', line, '|')
    print(f"└{'-' * (len(habitat[0]) + 2)}┘")

def getResults(parts):
    global images, habitat, seaMonsters, roughWaters

    habitat.clear()
    for i in range(side):
        row = [quadrans[p] for p in parts[i * side : (i+1) * side]]
        row = [[row[1:-1] for row in tile[1:-1]] for tile in row]
        for rows in zip(*row):
            habitat.append(''.join(rows))

    monsterCount = 0
    monsters = set()
    for row in range(len(habitat) - monsterHeight):
        for col in range(len(habitat[0]) - monsterWidth):
            if all(habitat[row + y][col + x] == '#' for x, y in monsterCoords):
                monsters.update((col + x, row + y) for x, y in monsterCoords)
                monsterCount += 1
 
    if not monsters:
        return False

    images = parts
    seaMonsters = monsters

    return True

def recurse(p):
    if len(p) != len(tiles):
        row, col = len(p) // side, len(p) % side
        for index in tiles.keys():
            if index in [i for i, j in p]:
                continue
            for j in range(8):
                if col > 0 and not all(p[-1] == q[0] for p, q in zip(quadrans[p[-1]], quadrans[(index, j)])):
                    continue
                if row > 0 and quadrans[p[len(p) - side]][-1] != quadrans[(index, j)][0]:
                    continue

                np = list(p)
                np.append((index, j))

                found = recurse(np)
                if found:
                    return
    else: return getResults(p)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1]:
        filename = sys.argv[1]
    else:
        filename = 'input.txt'
    with open(filename, "rt") as f:
        data = f.readlines()
        readTiles(data)

        side = int(len(tiles) ** 0.5)
        recurse([])

        # Part One:
        # What do you get if you multiply together the IDs of the four corner tiles?

        print('Part One:', images[0][0] * images[side - 1][0] * images[side * (side - 1)][0] * images[side * side - 1][0])

        # Part Two:
        # How many # are not part of a sea monster?

        roughWaters = sum(int(c == '#') for c in ''.join(habitat))
        print('Part Two:', roughWaters - len(seaMonsters))

        # Verbose
        addMonsters(habitat, seaMonsters)
        dumpHabitat(habitat)
