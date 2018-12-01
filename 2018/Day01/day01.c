// Day 01
//
// written by Thomas CARTON
//

#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <string.h>

unsigned int size = 0;
int *stack = NULL;

unsigned int count = 0;

bool addToStack(int value) {
    bool exists = false;

    for (unsigned int i = 0; i < count; ++i) {
        if (stack[i] == value) {
            exists = true;
        }
    }

    if (count + 1 >= size) {
        int *buffer = malloc(size << 3);
        memset(buffer, 0, size << 3);
        if (stack) {
            memcpy(buffer, stack, size << 2);
            free(stack);
        }
        stack = buffer;
        size <<= 1;
        printf("set stack size to %d\n", size);
    }

    stack[count++] = value;

    return exists;
}

int main(void) {
    int total = 0;

    int freq = -1;
    bool foundFreq = false;
    int same = -1;
    bool foundSame = false;

    size = 1024;
    stack = malloc(size << 2);
    memset(stack, 0, size << 2);
    addToStack(total);

	while (!foundSame) {
        FILE *file = fopen("input.txt", "r");
        if (file) {
            char *line = NULL;
            size_t len = 0;
            while (getline(&line, &len, file) != -1) {
                int value = 0;
                sscanf(line, "%d", &value);
                total += value;

                if (addToStack(total) && !foundSame) {
                    same = total;
                    foundSame = true;
                }
            }
            free(line);

			if (!foundFreq) {
				freq = total;
				foundFreq = true;
			}

            fclose(file);
        }
    }

    printf("\n- result 1 = %d", freq);
    printf("\n- result 2 = %d\n", same);
}
