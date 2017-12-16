// Day16 - dance
//
// written by Thomas CARTON
//

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#include "../common/input.h"

static const unsigned int kDancerCount = 16;

int main() {

	char dancer[kDancerCount + 1];

	for (unsigned int i = 0; i < kDancerCount; ++i) {
		dancer[i] = 'a' + i;
	}
	dancer[kDancerCount] = '\0';

	char *dance = NULL;
	unsigned int size = readInput("input.txt", &dance);

	char c, *s = dance;
	char step[6], *st = step;

	while (s - dance <= size) {
		c = *s++;
 		if (s - dance <= size && c != ',') {
			*st++ = c;
		} else {
			*st = '\0';
			st = step;

			// perform dance step
			printf("%10s", step);

			switch (step[0]) {

				case 's': {
					unsigned int sp;
					sscanf(&step[1], "%d", &sp);

					char temp[kDancerCount + 1];
					strcpy(temp, dancer);
					for (unsigned int i = 0; i < kDancerCount; ++i) {
						dancer[i] = i < sp ? temp[kDancerCount - sp + i] : temp[i - sp];
					}

					break;
				}

				case 'x': {
					unsigned int d1, d2;
					sscanf(&step[1], "%d/%d", &d1, &d2);

					char tmp = dancer[d1];
					dancer[d1] = dancer[d2];
					dancer[d2] = tmp;

					break;
				}

				case 'p': {
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

			printf("-- %s\n", dancer);
		}
	}

	printf("\ndancers: '%s'\n", dancer);

	return 0;
}
