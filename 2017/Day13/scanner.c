// Day 13
//
// written by Thomas CARTON
//

#include <stdlib.h>
#include <stdio.h>

#include "input.h"

typedef struct {
	unsigned int depth;
	unsigned int range;
} LAYER;

unsigned int parse(const char *buffer, unsigned int size, LAYER *layer) {
	char *s = (char *)buffer, *start = NULL, c;
	unsigned int index = 0;
	while ((c = *s++) && (s - buffer < size)) {
		if (start == NULL) {
			start = s - 1;
		}

		if (c == '\n') {
			unsigned int depth = 0;
			unsigned int range = 0;
			sscanf(start, "%d: %d", &depth, &range);

			printf("found: %d: %d\n", depth, range);
			if (layer) {

			}
			++index;
			start = NULL;
		}
	}

	return index;
}

int main() {
	char *data = NULL;
	unsigned int read = readInput("input.txt", &data);

	unsigned int length = parse(data, read, NULL);

	LAYER *layer = malloc(length * sizeof(LAYER));
	length = parse(data, read, layer);

	free(data);

	return 0;
}
