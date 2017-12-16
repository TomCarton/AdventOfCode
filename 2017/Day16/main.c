// Day16 - dance
//
// written by Thomas CARTON
//

#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <string.h>

#include "../common/input.h"

static const unsigned int kDancerCount = 16;
static const unsigned int kDanceCount = 1000000000;

void dance(char *dancer, const char *steps, unsigned int size, bool stats) {
	char temp[kDancerCount + 1];

	unsigned int sCount = 0;
	unsigned int xCount = 0;
	unsigned int pCount = 0;

	char c, *s = (char *)steps;
	char step[6], *st = step;

	while (s - steps <= size) {
		c = *s++;

 		if (s - steps <= size && c != ',') {
			*st++ = c;
		} else {
			*st = '\0';
			st = step;

			// perform dance step
			switch (step[0]) {

				case 's': {
					++sCount;

					unsigned int sp;
					sscanf(&step[1], "%d", &sp);

					strcpy(temp, dancer);
					for (unsigned int i = 0; i < kDancerCount; ++i) {
						dancer[i] = i < sp ? temp[kDancerCount - sp + i] : temp[i - sp];
					}

					break;
				}

				case 'x': {
					++xCount;

					unsigned int d1, d2;
					sscanf(&step[1], "%d/%d", &d1, &d2);

					char tmp = dancer[d1];
					dancer[d1] = dancer[d2];
					dancer[d2] = tmp;

					break;
				}

				case 'p': {
					++pCount;

					char p1, p2;
					sscanf(&step[1], "%c/%c", &p1, &p2);

					unsigned int d1, d2;
					for (unsigned int i = 0; i < kDancerCount; ++i) {
						if (dancer[i] == p1) d1 = i;
						if (dancer[i] == p2) d2 = i;
					}

					char tmp = dancer[d1];
					dancer[d1] = dancer[d2];
					dancer[d2] = tmp;

					break;
				}
			}
		}
	}

	if (stats) {
		printf ("s: %d, x: %d, p: %d\n", sCount, xCount, pCount);
	}
}

void prepare(char *dancers) {
	for (unsigned int i = 0; i < kDancerCount; ++i) {
		dancers[i] = 'a' + i;
	}
	dancers[kDancerCount] = '\0';
}

int main() {

	char *steps = NULL;
	unsigned int size = readInput("input.txt", &steps);

	char dancer[kDancerCount + 1];
	prepare(dancer);

	// initial
	char initial[kDancerCount + 1];
	prepare(initial);

	// get period
	unsigned int period = 0;
	for (period = 1; period < kDanceCount; ++period) {
		dance(dancer, steps, size, false);

		if (strcmp(dancer, initial) == 0) {
			break;
		}
	}
	printf("period = %d\n", period);

	// perform dance
	unsigned int remain = kDanceCount % period;

	for (unsigned int j = 0; j < remain; ++j) {
		dance(dancer, steps, size, false);
	}

	printf("\ndancers: '%s'\n", dancer);

	free(steps);

	return 0;
}
