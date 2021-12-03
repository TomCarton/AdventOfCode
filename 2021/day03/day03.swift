#!/usr/bin/env swift

import Foundation

public extension String {
	func character(at: Int) -> Character {
		self[index(startIndex, offsetBy: at)]
	}
}

// Advent of Code 2021
// Day 03

let content = try! String(contentsOfFile: "input.txt", encoding: .utf8)
let lines = content.components(separatedBy: "\n").filter { !$0.isEmpty }

let bitCount = lines[0].count

// Part One:
// What is the power consumption of the submarine?

var result: [Int] = .init(repeating: 0, count: bitCount)
for bit in 0..<bitCount {
    var count0 = 0, count1 = 0
    for line in 0..<lines.count {
        count0 += lines[line].character(at: bit) == "0" ? 1 : 0
        count1 += lines[line].character(at: bit) == "1" ? 1 : 0
    }

    result[bit] = count0 >= count1 ? 0 : 1
}

let gamma = Int(result.map(\.description).joined(), radix: 2)!
let epsilon = ~gamma & (Int(pow(2.0, Double(bitCount)) - 1))

print("Part One:", gamma * epsilon)

// Parto Two
// What is the life support rating of the submarine?

func shrubb(lines: [String], bit: Int, way: Bool) -> [String] {
    var count0 = 0, count1 = 0
    for line in 0 ..< lines.count {
        count0 += lines[line].character(at: bit) == "0" ? 1 : 0
        count1 += lines[line].character(at: bit) == "1" ? 1 : 0
    }

    let matchChar: Character = way ?
        (count0 > count1 ? "0" : "1") :
        (count0 <= count1 ? "0" : "1")

    return lines.filter { $0.character(at: bit) == matchChar }
}

func compute(_ lines: [String], _ way: Bool) -> Int {
    var temp = lines
    var bitPos = 0
    while temp.count > 1 {
        temp = shrubb(lines: temp, bit: bitPos, way: way)
        bitPos += 1
    }
    return Int(temp[0], radix: 2)!
}

let oxygen = compute(lines, true)
let co2 = compute(lines, false)

print("Part Two:", oxygen * co2)
