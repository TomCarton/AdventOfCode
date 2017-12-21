// 2015: Day 02
//
// writtent by Thomas CARTON
//

#include <stdlib.h>
#include <stdio.h>

#include "../../common/input.h"

static unsigned int prec = 1000000;

unsigned int wrappingSize(unsigned int side[3]) {
	unsigned int tmp;

	if (side[1] > side[2]) {
		tmp = side[2];
		side[2] = side[1];
		side[1] = tmp;
	}

	if (side[0] > side[1]) {
		tmp = side[1];
		side[1] = side[0];
		side[0] = tmp;
	}

	if (side[1] > side[2]) {
		tmp = side[2];
		side[2] = side[1];
		side[1] = tmp;
	}

	unsigned int size = 2 * (side[0] * side[1] + side[1] * side[2] + side[2] * side[0]);
	size += side[0] * side[1];

	unsigned int ribbonSize = 2 * (side[0] + side[1]);

	return size * prec + ribbonSize;
}

int main() {
	char *data = NULL;
	unsigned int read = readInput("input.txt", &data);

	if (read) {
		unsigned int totalSize = 0;

		char *s = data;
		while (s - data < read) {
			char c;
			unsigned int side[3];

			sscanf(s, "%dx%dx%d\n", &side[0], &side[1], &side[2]);
			while ((c = *s++) && c != '\n');

			unsigned int size = wrappingSize(side);
			totalSize += size;

			printf("%d x %d x %d = %d\n", side[0], side[1], side[2], size);
		}

		free(data);

		printf("\n");
		printf("Total size = %d\n", totalSize / prec);
		printf("Ribbon size = %d\n", totalSize % prec);
		printf("\n");
	}

	return 0;
}