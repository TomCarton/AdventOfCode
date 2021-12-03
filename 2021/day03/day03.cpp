// Advent of Code 2021
// Day 03
//

#include <vector>
#include <string>
#include <iostream>
#include <fstream>

int powerConsumption(std::vector<std::string> lines, char first, char second) {
    std::string consumption;

    for (int i = 0; i < (signed)lines[0].length(); ++i)
    {
        int count0 = 0, count1 = 0;
        for (int j = 0; j < (signed)lines.size(); ++j)
        {
            count0 += lines[j][i] == '0' ? 1 : 0;
            count1 += lines[j][i] == '1' ? 1 : 0;
        }

        consumption += count0 > count1 ? first : second;
    }

    return std::stoi(consumption, nullptr, 2);
}

int rating(std::vector<std::string> lines, int bit, char first, char second) {
    if (lines.size() == 1) {
        return std::stoi(lines[0], nullptr, 2);
    }

    int count0 = 0, count1 = 0;
    for (int j = 0; j < (signed) lines.size(); ++j)
    {
        count0 += lines[j][bit] == '0' ? 1 : 0;
        count1 += lines[j][bit] == '1' ? 1 : 0;
    }

    if (count0 > count1)
    {
        for (int j = 0; j < (signed)lines.size(); ++j)
        {
            if (lines[j][bit] == first)
                lines.erase(lines.begin() + j--);
        }
    }
    else
    {
        for (int j = 0; j < (signed)lines.size(); ++j)
        {
            if (lines[j][bit] == second)
                lines.erase(lines.begin() + j--);
        }
    }

    return rating(lines, bit + 1, first, second);
}

int main()
{
    std::vector<std::string> lines;

    std::ifstream file("input.txt");

    std::string line;
    while (std::getline(file, line))
        lines.push_back(line);

    // Part One:
    // What is the power consumption of the submarine?

    std::cout << "Part One: " << powerConsumption(lines, '0', '1') * powerConsumption(lines, '1', '0') << "\n";

    // Part Two:
    // What is the life support rating of the submarine?

    std::cout << "Part Two: " << rating(lines, 0, '0', '1') * rating(lines, 0, '1', '0') << '\n';

    return 0;
}
