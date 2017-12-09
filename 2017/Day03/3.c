// Day 3
//
// written by Thomas CARTON
//

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

#define PART 2
#define DISPLAY 0

//   1  
// 2   0
//   3

unsigned int *Map;
unsigned int MSide;
unsigned int MhSide;

void printMap() {
    for (unsigned int k = 0; k < 7 * MSide; ++k) printf("-"); printf("\n");

    for (unsigned int v = 0; v < MSide; ++v) {
        for (unsigned int u = 0; u < MSide; ++u) {
            unsigned int pos = (v * MSide) + u;
            printf("%5d ", Map[pos]);
        }
        printf("\n");
    }
}

void spiral(int value) {
    int dir = 0;
    int x = 0, y = 0;

    int v = 1;
    int dist = 0, step = 1;

    MSide = (int)ceil(sqrt(value)) | 1;
    MSide += 2;
    MhSide = MSide >> 1;
    printf("> %d, side = %d (%d)\n", value, MSide, MhSide);

    unsigned int size = (MSide + 2) * (MSide + 2) * sizeof(unsigned int);
    Map = malloc(size);
    memset(Map, 0, size);

    unsigned int pos = (MhSide * MSide) + MhSide;
    Map[pos] = 1;

    while (++v <= value) {
#   	if DISPLAY == -1
	        printMap();
#	   endif
        
        switch (dir) {
            case 0:
                dist = abs(++x);
                break;
            case 1:
                dist = abs(--y);
                break;
            case 2:
                dist = abs(--x);
                break;
            case 3:
                dist = abs(++y);
                break;
        }
        if (dist >= step) {
            dir = (dir + 1) % 4;
            if (dir == 0) {
                ++step;
            }
        }

        unsigned int pos = ((MhSide + y) * MSide) + MhSide + x;
        
#       if PART == 1
            Map[pos] = v;
#       elif PART == 2
            int sum = 0;
            sum += Map[((MhSide + y - 1) * MSide) + MhSide + x - 1];
            sum += Map[((MhSide + y - 1) * MSide) + MhSide + x];
            sum += Map[((MhSide + y - 1) * MSide) + MhSide + x + 1];

            sum += Map[((MhSide + y) * MSide) + MhSide + x - 1];
            sum += Map[((MhSide + y) * MSide) + MhSide + x + 1];

            sum += Map[((MhSide + y + 1) * MSide) + MhSide + x - 1];
            sum += Map[((MhSide + y + 1) * MSide) + MhSide + x];
            sum += Map[((MhSide + y + 1) * MSide) + MhSide + x + 1];

            Map[pos] = sum;
        
            if (sum > value) {
                printf("%d is larger than %d\n", sum, value);
                break;
            }
#       endif
    }

#   if DISPLAY == 1
        printMap();
#   endif

    printf("> coord: (%d, %d) = %d\n", x, y, abs(x) + abs(y));

    printf("\n\n");

    free(Map);
}

int main() {
//    spiral(1);
//    spiral(12);
//    spiral(23);
//    spiral(1024);
    spiral(312051);

    return 0;
}
