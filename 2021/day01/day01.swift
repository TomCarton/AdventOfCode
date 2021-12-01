#!/usr/bin/env swift

import Foundation

// Advent of Code 2021
// Day 01

let content = try! String(contentsOfFile: "input.txt", encoding: .utf8)
let lines = content.components(separatedBy: "\n").filter { !$0.isEmpty }
let values = lines.map { Int($0) ?? 0 }

// Part One:
// How many measurements are larger than the previous measurement?

var count = 0
for i in 1..<values.count {
    if values[i] > values[i - 1] {
        count += 1
    }
}    
print("Part One:", count)

// Part Two:
// How many sums are larger than the previous sum?

count = 0
for i in 3..<values.count {
    if values[i] > values[i - 3] {
        count += 1
    }
}    
print("Part Two:", count)
