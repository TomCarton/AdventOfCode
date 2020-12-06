//
//  day06.cpp
//  day06
//
//  Created by Thomas CARTON on 06/12/2020.
//

#include <iostream>
#include <fstream>

#include <set>


int main(int argc, char *argv[])
{
    std::ifstream file("input.txt");

    // Part One:
    // count the number of questions to which anyone answered "yes"
    int anyoneCount = 0;

    std::set<char> unik;

    unsigned int k = 0;
    std::string line;
    while (std::getline(file, line))
    {
        if (k == 0)
        {

        }

        if (line.empty())
        {
            anyoneCount += unik.size();
            unik.clear();
        } else {
            unik.insert(line.begin(), line.end());
        }

        ++k;
    }
    anyoneCount += unik.size();

    // Part Two:
    // count the number of questions to which everyone answered "yes"
    int everyoneCount = 0;

    std::cout << "Part One: " << anyoneCount << '\n';

    std::cout << "Part Two: " << everyoneCount << '\n';

    return 0;
}
