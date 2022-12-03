// Advent of Code 2022
// Day 01
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

static const char kDefaultFilename[] = "input.txt";
static const unsigned int kMaxBufferSize = 64;

void delay(int ms)
{
    clock_t endTime = clock() + 1000 * ms;
    while (clock() < endTime);
}

void dumpCursors(const char *line, unsigned int c1, unsigned int c2, unsigned int sum)
{
    printf("\033[H\033[J");

    printf("  "); for (unsigned i = 0; i < c1; ++i) printf(" "); printf("v\n");
    printf("  %s\n", line);
    printf("  "); for (unsigned i = 0; i < c2; ++i) printf(" "); printf("^\n");

    printf(" > %d\n\n", sum);

    delay(1);
}

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

    char *line, *p1, *p2, c, e;
    while((line = fgets(buffer, kMaxBufferSize, file)) != NULL)
    {
        unsigned int len = (unsigned int)strlen(line) - 1;
        line[len] = line[len] == '\n' ?: '\0';

        unsigned int half = len >> 1;

        p1 = line;
        p2 = line + half;

        do
        {
            dumpCursors(line, p1 - line, p2 - line, sum);

            c = *p2++;
            p1 += (e = 1 -!!*(p2 + 1));
            p2 -= e * half;
        }
        while(*p1 != c && p1 - line < half);

        sum += c - 38 - (~c & 32 ? 0 : 58);
    }

    printf("Part One: %d\n", sum);

    fclose(file);

    return 0;
}