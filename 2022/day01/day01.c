// Advent of Code 2022
// Day 01
//

#include <stdio.h>
#include <stdlib.h>

static const char kDefaultFilename[] = "input.txt";
static const unsigned int kMaxValueCharacters = 10;

int main(int argc, char *argv[])
{
    int max[3] = { 0, 0, 0 };

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

    int total = 0;

    int value;
    char line[kMaxValueCharacters];
    while(fgets(line, kMaxValueCharacters, file) != NULL)
    {
        value = atoi(line);
        total += value;

        if (value == 0)
        {
            if (total > max[0]) {
                max[2] = max[1];
                max[1] = max[0];

                max[0] = total;
            }

            total = 0;
        }
    }

    fclose(file);

    // Part One:
    // Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
    printf("Part One: %d\n", max[0]);

    // Part Two:
    // Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
    printf("Part Two: %d\n", max[0] + max[1] + max[2]);

    return 0;
}
