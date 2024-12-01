// day1
//

#include <iostream>
#include <map>

typedef std::pair<std::vector<int>, std::vector<int>> Input;

Input processInput()
{
    Input input;
    int left, right;

    while (std::cin >> left >> right)
    {
        input.first.push_back(left);
        input.second.push_back(right);
    }

    return input;
}

long long part1(Input input)
{
    std::sort(input.first.begin(), input.first.end());
    std::sort(input.second.begin(), input.second.end());

    long long total_distance = 0;
    for (unsigned int i = 0; i < input.first.size(); ++i)
    {
        total_distance += std::abs(input.first[i] - input.second[i]);
    }

    return total_distance;
}

long long part2(Input input)
{
    std::map<int, int> count;

    for(int number : input.second)
    {
        ++count[number];
    }

    long long score = 0;
    for (int number : input.first)
    {
        score += number * count[number];
    }

    return score;
}

int main(int argc, char *argv[])
{
    std::freopen(argc == 1 ? "input.txt" : argv[1], "r", stdin);

    Input input = processInput();
    std::cout << "  Part One: " << part1(input) << '\n';
    std::cout << "  Part Two: " << part2(input) << '\n';
}
