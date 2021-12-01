// Advent of Code 2021
// Day 01
//

#include <vector>
#include <iostream>
#include <fstream>

template <typename T = int>
std::vector<T> ReadDataAs(std::ifstream& stream)
{
    std::vector<T> ret;

    T n = 0;
    while (stream >> n)
        ret.push_back(n);

    return ret;
}

int main()
{
    std::ifstream in("input.txt");
    std::vector<int> heights = ReadDataAs<int>(in);

    // Part One:
    // How many measurements are larger than the previous measurement?
    
    int count = 0;
    for (unsigned int i = 1; i < heights.size(); ++i)
    {
        if (heights[i - 1] < heights[i])
          ++count;
    }

    std::cout << "Part One: " << count << "\n";

    // Part Two:
    // How many sums are larger than the previous sum?

    count = 0;
    for (unsigned int i = 3; i < heights.size(); ++i)
    {
        if (heights[i - 1] + heights[i - 2] + heights[i - 3] < heights[i] + heights[i - 1] + heights[i - 2])
            ++count;
    }

    std::cout << "Part Two: " << count << "\n";

    return 0;
}
