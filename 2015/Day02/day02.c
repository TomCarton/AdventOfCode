// Day02.x
//
#include <stdio.h>
#include <stdlib.h>

uint64_t rdtsc()
{
    unsigned int lo, hi;
    __asm__ __volatile__ ("rdtsc" : "=a" (lo), "=d" (hi));
    return ((uint64_t)hi << 32) | lo;
}

void perform(const char *buffer)
{
    char c;
    char *s = (char *)buffer;

    unsigned int value = 0;
    unsigned int side[3] = {0, 0, 0};
    unsigned int currentSide = 0;

    unsigned int paper = 0;
    unsigned int ribbon = 0;

    uint64_t t0 = rdtsc();

    while ((c = *s++))
    {
        if (c >= '0' && c <= '9')
        {
            value *= 10;
            value += c - '0';
        }
        else
        {
            side[currentSide++] = value;
            value = 0;

            if (currentSide > 2)
            {
                // sort sides
                if (side[1] > side[2])
                {
                    int tmp = side[1];
                    side[1] = side[2];
                    side[2] = tmp;
                }
                if (side[0] > side[1])
                {
                    int tmp = side[0];
                    side[0] = side[1];
                    side[1] = tmp;
                }
                if (side[1] > side[2])
                {
                    int tmp = side[1];
                    side[1] = side[2];
                    side[2] = tmp;
                }

                // get faces
                int face1 = side[0] * side[1];
                int face2 = side[0] * side[2];
                int face3 = side[1] * side[2];

                paper += 2 * (face1 + face2 + face3) + face1;
                ribbon += 2 * (side[0] + side[1]) + side[0] * side[1] * side[2];

                currentSide = 0;
            }
        }
    }

    uint64_t t1 = rdtsc();
    printf("> %llu cycles taken\n\n", t1 - t0);

    // Part One:
    // How many total square feet of wrapping paper should they order?
    printf("Part One: %d\n", paper);

    // Part Two:
    // How many total square feet of wrapping paper should they order?
    printf("Part Two: %d\n", ribbon);
}

void *readFile(const char *filename)
{
    char *buffer = NULL;

    FILE *file = fopen(filename, "r");
    if (file)
    {
        fseek(file, 0, SEEK_END);
        int filesize = ftell(file);
        fseek(file, 0, SEEK_SET);

        if (filesize > 0)
            buffer = (char *)malloc(filesize + 1);

        if (buffer != NULL)
        {
            size_t read = fread(buffer, 1, filesize, file);
            if (read != filesize)
            {
                free(buffer);
                buffer = NULL;
            }

            buffer[filesize] = '\0';
        }

        fclose(file);
    }

    return buffer;
}

int main(int argc, char *argv[])
{
    const char kDefaultFilename[] = "input.txt";
    char *filename = argc > 1 ? argv[1] : (char *)&kDefaultFilename;

    char *buffer = (char *)readFile(filename);
    if (buffer == NULL)
    {
        fprintf(stderr, "!Error: unable to read file \"%s\".\n", filename);
        return -1;
    }

    perform(buffer);

    free(buffer);

    return 0;
}