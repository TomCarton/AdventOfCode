// Day 11
//
// written by Thomas CARTON
//

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

char *buffer = NULL;
unsigned int bufferSize = 0;

unsigned int readInput(const char *filename) {
	unsigned int read = 0;

	FILE *file = fopen(filename, "r");

	if (file) {
		fseek(file, 0, SEEK_END);
		bufferSize = ftell(file);
		fseek(file, 0, SEEK_SET);

		if (bufferSize) {
			buffer = malloc(bufferSize);
			if (buffer) {
				read = fread(buffer, 1, bufferSize, file);
			}
		}

		fclose(file);
	}

	return read;
}

int max(int a, int b, int c) {
	int m = 0;

	if (a > m) {
		m = a;
	}
	if (b > m) {
		m = b;
	}
	if (c > m) {
		m = c;
	}

	return m;
}

int hexDistance(int x0, int y0, int x1, int y1) {
	int dx = x1 - x0;
	int dy = y1 - y0;

	int d = abs(dx) + abs(dy);
	d /= 2;

	return d;
}

int main() {

	unsigned int read = readInput("input.txt");

	int x = 0, y = 0;
	int maxDist = 0;

	char *s = buffer;
	while (s - buffer < read) {
		char dir[4];
		char *d = dir, c;
		while ((c = *s++) && c != ',') {
			if (c >= 'a' && c <= 'z') {
				*d++ = c;
			}
		}
		*d = '\0';

		if (strcmp(dir, "ne") == 0) {
			--x;
			--y;
		} else if (strcmp(dir, "n") == 0) {
			--y;
			--y;
		} else if (strcmp(dir, "nw") == 0) {
			++x;
			--y;
		} else if (strcmp(dir, "se") == 0) {
			--x;
			++y;
		} else if (strcmp(dir, "s") == 0) {
			++y;
			++y;
		} else if (strcmp(dir, "sw") == 0) {
			++x;
			++y;
		}

		int dist = hexDistance(0, 0, x, y);
		if (dist > maxDist) {
			maxDist = dist;
		}

		printf(". %s (%d, %d) %d\n", dir, x, y, dist);
	}

	printf("\nMax distance = %d\n", maxDist);

	return 0;
}