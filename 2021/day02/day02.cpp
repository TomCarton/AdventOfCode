// Advent of Code 2021
// Day 02
//

#include <vector>
#include <iostream>
#include <fstream>
#include <string>

struct command
{
    std::string verb;
    int amount;
};

int main()
{
    std::vector<command> commands;

    std::ifstream file("input.txt");
 
    std::string line;
    while (std::getline(file, line))
    {
        size_t separator = line.find_first_of(' ');
        commands.push_back({ line.substr(0, separator), std::stoi(line.substr(separator + 1)) });
    }

    // Part One:
    // What do you get if you multiply your final horizontal position by your final depth?
    int position = 0;
    int depth = 0;

    for(auto& command : commands)
    {
        if (command.verb == "down") depth += command.amount;
        else if(command.verb == "up") depth -= command.amount;

        else if (command.verb == "forward") position += command.amount;
    }

    std::cout << "Part One: " << position * depth << "\n";

    // Part Two:
    // What do you get if you multiply your final horizontal position by your final depth?

    int aim = 0;
    position = 0;
    depth = 0;

    for(auto& command : commands)
    {
        if (command.verb == "down") aim += command.amount;
        else if(command.verb == "up") aim -= command.amount;

        else if (command.verb == "forward") { position += command.amount; depth += command.amount * aim; }
    }

    std::cout << "Part Two: " << position * depth << "\n";

    return 0;
}
