// day02.cpp
//

#include <iostream>
#include <fstream>
#include <string>

// 4-14 d: lxdmddfddddddd
int main(int argc, char *argv[])
{
    unsigned int countP1 = 0, countP2 = 0;

    std::ifstream file("input.txt");

    unsigned char chars[26];
    std::string line;
    while (std::getline(file, line)) {
        memset(chars, 0, sizeof(chars));

        size_t delim1 = line.find('-');
        size_t delim2 = line.find(':');

        unsigned int min = atoi(line.substr(0, delim1).c_str());
        unsigned int max = atoi(line.substr(delim1 + 1, delim2).c_str());
        char letter = line[delim2 - 1];

        const char *password = line.c_str() + delim2 + 2;
        for (unsigned int i = 0; i < strlen(password); ++i) ++chars[(password[i] | ' ') - 'a'];

        unsigned int occurences = chars[letter - 'a'];
        if (occurences >= min && occurences <= max)
            ++countP1;

        if ((password[min - 1] == letter) ^ (password[max - 1] == letter))
            ++countP2;
   }

    std::cout << "Part One: " << countP1 << '\n';
    std::cout << "Part Two: " << countP2 << '\n';

    return 0;
}
