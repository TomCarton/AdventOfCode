// day01.cpp
//

#include <fstream>
#include <iostream>
#include <string>

#include <bits/stdc++.h>

int main(int argc, char *argv[])
{
    using namespace std;

    string filename("input.txt");
    if (argc > 1)
    {
        filename = argv[1];
    }

    ifstream file { filename };
    if (!file)
    {
        cerr << "!error: " << filename << " could not be opened for reading!\n";
        return 1;
    }

    vector<string> lines;
    string line;
    while (getline(file, line))
    {
        lines.push_back(line);
    }

    int p1 = 0;
    for (string line : lines)
    {
        vector<int> v;
        for (char c : line)
        {
            if (isdigit(c))
            {
                v.push_back(c - '0');
            }
        }

        p1 += v.front() * 10 + v.back();
    }

    cout << "  Part One: " << p1 << '\n';

    int p2 = 0;
    vector<string> numbers { "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" };
    for (string line : lines)
    {
        vector<int> v;

        for (int i = 0; i < line.length(); ++i)
        {
            char c = line[i];
            if (isdigit(c))
            {
                v.push_back(c - '0');
            }
            else
            {
                for (int n = 0; n < numbers.size(); ++n)
                {
                    if (i + numbers[n].length() > line.length())
                        continue;

                    if (line.substr(i, numbers[n].length()) == numbers[n])
                    {
                        v.push_back(n);
                        break;
                    }
                }
            }
        }

        p2 += v.front() * 10 + v.back();
    }

    cout << "  Part Two: " << p2 << '\n';

    return 0;
}
