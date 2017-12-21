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
	bool alive;

	long int p[3];
	long int v[3];
	long int a[3];

	unsigned long int distance;
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

		unsigned int particleCount = 0;
		while (getLine(&in, line)) {
			Particule *p = &particule[particleCount++];

			sscanf(line, "p=<%ld,%ld,%ld>, v=<%ld,%ld,%ld>, a=<%ld,%ld,%ld>", 
				&p->p[0], &p->p[1], &p->p[2],
				&p->v[0], &p->v[1], &p->v[2],
				&p->a[0], &p->a[1], &p->a[2]);

			p->alive = true;
			p->distance = labs(p->p[0]) + labs(p->p[1]) + labs(p->p[2]);
		}

		unsigned long int tickCount = 10000;
		unsigned int mini;
		unsigned long int mind;
		unsigned int collision = 0;
		for (unsigned long int tick = 0; tick < tickCount; ++tick) {
			if (tick % 100 == 0) {
				printf("\033[H\033[J");
				printf("total: %02d%%\n #%d, d = %ld\n %d collision%s\n\n", (unsigned int)(tick * 100 / tickCount) + 1, mini, mind, collision, collision > 1 ? "s" : "");
			}

			mini = 0;
			mind = labs(particule[mini].p[0]) + labs(particule[mini].p[2]) + labs(particule[mini].p[2]);

			// tick update
			for (unsigned int i = 0; i < particleCount; ++i) {
				Particule *p = &particule[i];
				// if (p->alive) {

					p->v[0] += p->a[0];
					p->v[1] += p->a[1];
					p->v[2] += p->a[2];

					p->p[0] += p->v[0];
					p->p[1] += p->v[1];
					p->p[2] += p->v[2];

					p->distance = labs(p->p[0]) + labs(p->p[1]) + labs(p->p[2]);
					if (p->distance < mind) {
						mind = p->distance;
						mini = i;
					}
				// }
			}

			// collide
			for (unsigned int i = 0; i < particleCount; ++i) {
				Particule *p1 = &particule[i];
				if (p1->alive) {
					for (unsigned int j = i + 1; j < particleCount; ++j) {
						Particule *p2 = &particule[j];
						if (p2->alive) {
							if (p1->p[0] == p2->p[0] && p1->p[1] == p2->p[1] && p1->p[2] == p2->p[2]) {
								p1->alive = false;
								p2->alive = false;
								++collision;
							}
						}
					}
				}
			}
		}
		printf("Part one: min i = #%d (min d = %ld)\n", mini, mind);

		unsigned int alive = 0;
		for (unsigned int i = 0; i < particleCount; ++i) {
			Particule *p = &particule[i];
			if (p->alive) ++alive;
		}
		printf("Part two: alive count = #%d\n", alive);

		free(particule);		
	}

	printf("\n");

	free(input);

	return 0;
}
