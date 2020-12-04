// day03.cpp
//

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

unsigned int performSlope(const char *field, unsigned int width, unsigned int height, unsigned int dx, unsigned int dy)
{
    unsigned int treeCount = 0;

    unsigned int x = 0;
    unsigned int y = 0;

    do
    {
        treeCount += 1 - (field[y * (width + 1) + x] - 0x23) / 11;
        x = (x + dx) % width;
        y += dy;
    } while (y < height);

    return treeCount;
}

int main(int argc, char *argv[])
{
    std::ifstream f("input.txt");
    std::string content((std::istreambuf_iterator<char>(f)), std::istreambuf_iterator<char>());

    const char *field = content.c_str();
    unsigned int fieldSize = content.length();

    unsigned int width = content.find(0x0A);
    unsigned int height = fieldSize / (width + 1);

    unsigned int treeTotal = performSlope(field, width, height, 3, 1);
    std::cout << "Part One: " << treeTotal << '\n';

    unsigned int treeCount = performSlope(field, width, height, 1, 1);
    treeTotal *= treeCount;
    treeCount = performSlope(field, width, height, 5, 1);
    treeTotal *= treeCount;
    treeCount = performSlope(field, width, height, 7, 1);
    treeTotal *= treeCount;
    treeCount = performSlope(field, width, height, 1, 2);
    treeTotal *= treeCount;
    std::cout << "Part Two: " << treeTotal << '\n';

    return 0;
}
