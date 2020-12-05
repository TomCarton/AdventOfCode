// day05 .cpp
//
// Advent of Code 2020
//

#include <iostream>
#include <fstream>
#include <string>
#include <vector>

int main(int argc, char *argv[])
{
    std::vector<uint16_t> seats;

    std::ifstream file("input.txt");

    std::string line;
    while (std::getline(file, line))
    {
        unsigned int seatId = 0;
        for (unsigned int k = 0; k < 10; ++k)
            seatId = (seatId << 1) | (~line[k] & 4);

        seats.push_back(seatId >> 2);
    }

    // Part One:
    // What is the highest seat ID on a boarding pass?

    uint16_t highestSeatId = *std::max_element(seats.begin(), seats.end());

    std::cout << "Part One: " << highestSeatId << '\n';

    // Part Two:
    // What is the ID of your seat?

    auto occupiedSeats = std::vector<bool>(highestSeatId);
    for (uint16_t id : seats)
        occupiedSeats[id] = true;

    uint16_t id = 0;
    for (id = 1; id < highestSeatId - 1; ++id)
        if (occupiedSeats[id - 1] && !occupiedSeats[id] && occupiedSeats[id + 1])
            break;

    std::cout << "Part Two: " << id << '\n';

    return 0;
}
