// Day 3
//
// written by Thomas CARTON
//

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

#define VERSION 2

//   1  
// 2   0
//   3

void coords(int value) {
	int dir = 0;
	int x = 0, y = 0;

	int v = 0;
	int dist, step = 1;

#	if VERSION == 2
		unsigned int side = (int)ceil(sqrt(value)) | 1;
		unsigned int hside = side >> 1;
		printf("> %d, side = %d (%d)\n", value, side, hside);

		unsigned int size = (side + 2) * (side + 2) * sizeof(unsigned int);
		unsigned int *map = malloc(size);
		memset(map, 0, size);
		map[hside * side + hside] = 1;
		int M = 0;
#	endif

	while (++v < value) {
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

#		if VERSION == 2
			unsigned int pos = ((hside + y + 1) * side) + (hside + x + 1);

			printf("-- (%d,%d) -- pos = %d\n", x, y, pos);

			if (map[pos] == 0) {
				unsigned int v = map[pos - 1 - side];
				v += map[pos - side];
				v += map[pos + 1 - side];
				v += map[pos - 1];
				v += map[pos + 1];
				v += map[pos - 1 + side];
				v += map[pos + side];
				v += map[pos + 1 + side];

				map[pos] = v;
				// printf("... %d\n", v);

				if (v > value) {
					M = v;
				}
			}
#		endif
	}

#	if VERSION == 1
		printf("> coord: (%d, %d) = %d\n", x, y, abs(x) + abs(y));
#	elif VERSION == 2
		printf("> value: %d\n", M);
		free(map);
#	endif
}

int main() {
	coords(1);
	coords(12);
	coords(23);
	// coords(1024);
	// coords(312051);

	return 0;
}