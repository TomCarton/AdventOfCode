// Advent of Code 2020
// Day 17

const input = require('fs')
    .readFileSync('input.txt', 'utf-8')
    .split('\n')
    .map((x, i) =>
        x.split('')
            .map((y, j) => y==='#' ? `${i},${j},0,0` : null)
            .filter(x => x !== null)
    )
    .flat();

const toString = coord => coord.join(',');
const fromString = str => str.split(',').map(x => parseInt(x));
const isBetween = (val, min, max) => val >= min && val <= max

const getVectors = dim => {
    if (dim === 1) {
        return [[-1], [0], [1]];
    }
    return getVectors(dim-1)
        .map(v => [-1, 0, 1].map(x => [x, ...v]))
        .flat()
}

const getOuterVectors = dim =>
    getVectors(dim)
        .filter(v => v.some(x => x !== 0)); // not the zero vector

const adjacent = vectors => coord => {
    const [x, y, z, w] = fromString(coord);
    return vectors.map(([s, t, u=0, v=0]) => toString([x+s, y+t, z+u, w+v]));
}

const adjacentSet = (vectors, coords) => new Set(
    [...coords]
        .map(adjacent(vectors))
        .flat()
        .filter(x => !coords.has(x))
);

const activeAdjacent = (vectors, active, coord) => adjacent(vectors)(coord).reduce((n, c) => active.has(c) ? n+1: n, 0)

const next = (vectors, active) => {
    const inactive = adjacentSet(vectors, active);

    const stillActive = [...active].filter(coordinates => isBetween(activeAdjacent(vectors, active, coordinates), 2, 3 ));
    const newActive = [...inactive].filter(coordinates => isBetween(activeAdjacent(vectors, active, coordinates), 3, 3 ));

    return new Set([...stillActive, ...newActive]);
};

const simulate = (vectors, initial) => {
    let active = new Set(initial);

    for (let i=0; i<6; i++) {
        active = next(vectors, active);
    }

    return active.size;
}

console.log("Part One: ", simulate(getOuterVectors(3), input));
console.log("Patr Two: ", simulate(getOuterVectors(4), input));