// Day 3
//
// written by Thomas CARTON
//

#include <stdlib.h>
#include <stdio.h>

//   1  
// 2   0
//   3

void coords(int value) {
	int dir = 0;
	int x = 0, y = 0;

	int v = 1;
	int dist, step = 1;

	while (v < value) {
		// printf("coord: (%d, %d)\n", x, y);
		v += 1;
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
	}

	printf("> coord: (%d, %d) = %d\n", x, y, abs(x) + abs(y));
}

int main() {
	coords(1);
	coords(12);
	coords(23);
	coords(1024);
	coords(312051);

	return 0;
}