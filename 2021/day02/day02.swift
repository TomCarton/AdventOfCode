#!/usr/bin/env swift

import Foundation

// Advent of Code 2021
// Day 02

let content = try! String(contentsOfFile: "input.txt", encoding: .utf8)
let lines = content.components(separatedBy: "\n").filter { !$0.isEmpty }
let strings = lines.map { $0.split(separator: " ") }
let commands = strings.map { ($0[0], Int($0[1]) ?? 0) }

// Part One:
// What do you get if you multiply your final horizontal position by your final depth?
var position = 0
var depth = 0

for c in commands {
    switch c.0 {
        case "down":
            depth += c.1
        case "up":
            depth -= c.1

        case "forward":
            position = position + c.1

        default:
            print("Unknown command: \(c.0)")
    }
}

print("Part One:", position * depth)

// Part Two:
// What do you get if you multiply your final horizontal position by your final depth?
var aim = 0
position = 0
depth = 0

for c in commands {
    switch c.0 {
        case "down":
            aim += c.1
        case "up":
            aim -= c.1
        case "forward":
            position += c.1
            depth += c.1 * aim

        default:
            print("Unknown command: \(c.0)")
    }
}

print("Part Two:", position * depth)
