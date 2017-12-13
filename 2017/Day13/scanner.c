// Day 13
//
// written by Thomas CARTON
//

#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

#include "input.h"

typedef struct {
	unsigned int depth;
	unsigned int range;
} LAYER;

LAYER *Layer = NULL;
unsigned int LayerCount = 0;

unsigned int MaxDepth = 0;

unsigned int Scanner = 0;
unsigned int Packet = 0;

unsigned int parse(const char *buffer, unsigned int size, LAYER *layer) {
	char *s = (char *)buffer, *start = NULL;
	unsigned int index = 0;
	do {
		char c = *s++;

		if (start == NULL) {
			start = s - 1;
		}

		if (c == '\n' || c == 0 || s - buffer == size) {
			unsigned int depth = 0;
			unsigned int range = 0;
			sscanf(start, "%d: %d", &depth, &range);

			if (depth > MaxDepth) {
				MaxDepth = depth;
			}

			if (layer) {
				layer[index].depth = depth;
				layer[index].range = range;
			}

			start = NULL;
			++index;
		}
	} while (s - buffer < size);

	return index;
}

unsigned int scannerPosition(unsigned int index, unsigned int range) {
	unsigned int pos = index % range;

	return pos;
}

void dumpLayers(unsigned int depth) {
	printf("\n");

	if (depth > 0) {
		depth = MaxDepth < depth ? MaxDepth : depth;
	} else {
		depth = MaxDepth;
	}
	++depth;

	// 0:  0   1   2   3   4   5   6   7   8  ...
	for (unsigned int i = 0; i < depth; ++i) {
		printf("%2d  ", i);
	}
	printf("\n");

	// x: [S] [S] ( ) [ ] ... [ ]     [ ] [S] ...
	for (unsigned int d = 0; d < 5; ++d) {
		LAYER *layer = Layer;

		for (unsigned int l = 0; l < depth; ++l) {
			if (l > layer->depth) {
				++layer;
			}
			if (l < layer->depth) {
				if (d == 0) {
					printf(d == 0 && l == Packet ? "(.) " : "... ");
				} else {					
					printf("    ");
				}
			} else if (scannerPosition(Scanner, layer->range) == d) {
				printf(d == 0 && l == Packet ? "(S) " : "[S] ");
			} else if (d < layer->range) {
				printf(d == 0 && l == Packet ? "( ) " : "[ ] ");
			} else {
				printf("    ");
			}
		}

		printf("\n");
	}
}

int main() {
	char *data = NULL;
	unsigned int read = readInput("input.txt", &data);

	unsigned int length = parse(data, read, NULL);

	Layer = malloc(length * sizeof(LAYER));
	parse(data, read, Layer);

	free(data);

	for (unsigned int k = 0; k < MaxDepth + 1; ++k) {
		printf("Picosecond %d:\n", k);
		bool caught = false;

		dumpLayers(8);

		for (unsigned int i = 0; i < length; ++i) {
			if (Packet != Layer[i].depth) continue;

			if (scannerPosition(Scanner, Layer[i].range) == 0) {
				caught = true;
			}
		}

		++Scanner;
		dumpLayers(8);

		if (caught) {
			printf("### Caught\n");
		}

		++Packet;

		printf("\n");
	}

	free(Layer);

	return 0;
}
