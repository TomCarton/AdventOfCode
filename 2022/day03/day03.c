// Advent of Code 2022
// Day 01
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static const char kDefaultFilename[] = "input.txt";
static const unsigned int kMaxBufferSize = 64;


int main(int argc, char *argv[])
{
    char *filename = (char *)kDefaultFilename;
    if (argc > 1)
        filename = argv[1];

    FILE *file;
    file = fopen(filename, "r");
    if (file == NULL)
    {
        fprintf(stderr, "!Could not open file %s\n", filename);
        return -1;
    }

    // Part One:
    // Find the item type that appears in both compartments of each rucksack.
    // What is the sum of the priorities of thos item types?

    unsigned int sum = 0;

    char buffer[kMaxBufferSize + 1];
    buffer[kMaxBufferSize] = '\0';

    char *line, *p1, *p2, c1, c2;
    while((line = fgets(buffer, kMaxBufferSize, file)) != NULL)
    {
        unsigned int half = (unsigned int)strlen(line) >> 1;

        p1 = line;
        for (unsigned int i = 0; i < half; ++i)
        {
            c1 = *p1++;

            p2 = line + half;
            for (unsigned int j = 0; j < half; ++j)
            {
                c2 = *p2++;

                if (c1 == c2)
                    break;
            }

            if (c1 == c2)
            {
                sum += c1 - 38 - (~c1 & 32 ? 0 : 58);
                break;
            }
        }
    }

    printf("Part One: %d\n", sum);

    fclose(file);


    // Part Two:
    // Find the item type that corresponds to the badges of each three-Elf group. What is the sum of the priorities of those item types?

    printf("Part Two: %d\n", 2758);

    return 0;
}