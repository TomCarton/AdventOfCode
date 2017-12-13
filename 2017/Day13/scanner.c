// Day 13
//
// written by Thomas CARTON
//

#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

#include "input.h"

#define kIncrement "   "

typedef struct {
	unsigned int depth;
	unsigned int range;
} LAYER;

LAYER *Layer = NULL;
unsigned int LayerCount = 0;

unsigned int MaxDepth = 0;

unsigned int Scanner, Packet;

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
	unsigned int pos;

#	if 0
		// modulo
		pos = index % range;
#	else
		// back and forth
		--range;
		pos = index % (range << 1);
		if (pos > range) {
			pos = range - (pos - range);
		}
#	endif

	return pos;
}

void dumpLayers(unsigned int depth, bool show) {
	if (depth > 0) {
		depth = MaxDepth < depth ? MaxDepth : depth;
	} else {
		depth = MaxDepth;
	}
	++depth;

	// 0:  0   1   2   3   4   5   6   7   8  ...
	printf(kIncrement);
	for (unsigned int i = 0; i < depth; ++i) {
		printf("%2d  ", i);
	}
	printf("\n");

	// x: [S] [S] ( ) [ ] ... [ ]     [ ] [S] ...
	for (unsigned int d = 0; d < 5; ++d) {
		LAYER *layer = Layer;

		printf(kIncrement);
		
		for (unsigned int l = 0; l < depth; ++l) {
			if (l > layer->depth) {
				++layer;
			}
			if (l < layer->depth) {
				if (d == 0) {
					printf(show && d == 0 && l == Packet ? "(.) " : "... ");
				} else {					
					printf("    ");
				}
			} else if (scannerPosition(Scanner, layer->range) == d) {
				printf(show && d == 0 && l == Packet ? "(S) " : "[S] ");
			} else if (d < layer->range) {
				printf(show && d == 0 && l == Packet ? "( ) " : "[ ] ");
			} else {
				printf("    ");
			}
		}

		printf("\n");
	}
}

bool runPacket(unsigned int delay, unsigned int picosecond, bool display) {
	unsigned int severity = 0;

	Scanner = delay;
	Packet = 0;

	if (display) {
		printf("\n=================================================================++\n");
		printf(" Run with delay %d\n", delay);
		printf("===================================================================\n\n");

		printf(kIncrement "Initial state:\n");
		dumpLayers(8, false);

	}

	for (unsigned int k = 0; k < MaxDepth + 1; ++k) {
		if (display) {
			printf(kIncrement "Picosecond %d:\n", k + delay);

			dumpLayers(8, true);
		}

		for (unsigned int i = 0; i < LayerCount; ++i) {
			if (Packet != Layer[i].depth) continue;

			if (i != 0 && scannerPosition(Scanner, Layer[i].range) == 0) {
				severity += Layer[i].depth * Layer[i].range;
			}
		}

		++Scanner;
		if (display) {
			dumpLayers(8, true);
			printf("\n");
		}

		++Packet;
	}

	if (display && severity > 0) printf("### CAUGHT! ### Severity = %d ###\n\n", severity);

	return severity > 0;
}

int main() {

	char *data = NULL;
	unsigned int read = readInput("input.txt", &data);

	LayerCount = parse(data, read, NULL);
	Layer = malloc(LayerCount * sizeof(LAYER));
	parse(data, read, Layer);

	free(data);

	unsigned int d = 0; {
	// for (unsigned int d = 0; d < 100; ++d) {
		if (runPacket(d, 6, true) == false) {
			printf("should delay %d picosecond%s...\n", d, d > 1 ? "s" : "");
			// break;
		}
	}

	free(Layer);

	return 0;
}
