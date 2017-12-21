// Day 20
//
// written by Thomas CARTON
//

#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <string.h>

#include "../../Common/input.h"

typedef struct {
	long int p[3];
	long int v[3];
	long int a[3];
} Particule;

int main() {

	char *input = NULL;
	readInput("input.txt", &input);

	unsigned int lineCount = 0;
	char *in = input;
	while (getLine(&in, NULL)) ++lineCount;

	Particule *particule = malloc(lineCount * sizeof(Particule));
	if (particule) {
		char line[kLineMaxLength + 1];
		in = input;

		unsigned int count = 0;
		while (getLine(&in, line)) {
			Particule *p = &particule[count++];

			sscanf(line, "p=<%ld,%ld,%ld>, v=<%ld,%ld,%ld>, a=<%ld,%ld,%ld>", 
				&p->p[0], &p->p[1], &p->p[2],
				&p->v[0], &p->v[1], &p->v[2],
				&p->a[0], &p->a[1], &p->a[2]);
		}

		unsigned long int tickCount = 1000000;
		unsigned int mini;
		unsigned long int mind;
		for (unsigned long int tick = 0; tick < tickCount; ++tick) {
			if (tick % 100 == 0) {
				printf("\033[H\033[J");
				printf("total: %02d%% - #%d, d = %ld \n\n", (unsigned int)(tick * 100 / tickCount) + 1, mini, mind);
			}

			mini = 0;
			mind = labs(particule[mini].p[0]) + labs(particule[mini].p[2]) + labs(particule[mini].p[2]);

			for (unsigned int i = 0; i < count; ++i) {

				Particule *p = &particule[i];

				p->v[0] += p->a[0];
				p->v[1] += p->a[1];
				p->v[2] += p->a[2];

				p->p[0] += p->v[0];
				p->p[1] += p->v[1];
				p->p[2] += p->v[2];

				unsigned long int d = labs(p->p[0]) + labs(p->p[1]) + labs(p->p[2]);
				if (d < mind) {
					mind = d;
					mini = i;
				}
			}
		}

		printf("mind = %ld, mini = #%d\n\n", mind, mini);

		free(particule);		
	}

	free(input);

	return 0;
}
