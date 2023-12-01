// day01.c
//

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    char *filename = "input.txt";
    if (argc > 1)
        filename = argv[1];

    FILE *file = fopen(filename, "r");
    if (file == NULL)
    {
        printf("!Error: unable to open file: %s\n", filename);

        return 1;
    }

    fseek(file, 0, SEEK_END);
    long size = ftell(file);
    fseek(file, 0, SEEK_SET);

    unsigned char *data = (unsigned char *)malloc(size);
    size_t read = fread(data, sizeof(unsigned char), size, file);
    if (read != size)
    {
        printf("!Error: unable to read file: %s [%ld/%ld]\n", filename, read, size);
        
        fclose(file);
        return 1;
    }
    fclose(file);

    int p1 = 0;
    int p2 = 0;

    int first = -1;
    int second = -1;
    
    unsigned char *line = data;
    unsigned char *p = line;

    char c = 0;
    do
    {
        c = *p++;

        if (c == '\n' || c == '\0')
        {
            p[-1] = '\0';
            if (first != -1 && second != -1)
            {
                p1 += first * 10 + second;
                first = second = -1;
            }

            line = p;
        }
        else if (c >= '0' && c <= '9')
        {
            if (first == -1)
            {
                first = second = c - '0';
            }
            else
            {
                second = c - '0';
            }
        }
    } while (c != '\0');


    printf("  Part One: %d\n", p1);

    free(data);
    return 0;
}
