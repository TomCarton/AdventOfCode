// Day 15
//
// written by Thomas CARTON
//

#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

unsigned long generatorA, generatorB;

unsigned long step(unsigned long value, unsigned long factor) {
	return (value * factor) % 2147483647;
}

unsigned int iterate(unsigned int steps, bool mode) {
	unsigned int count = 0;

	// Generator A starts with 703
	unsigned long generatorA = 703;
	// Generator B starts with 516
	unsigned long generatorB = 516;

	for (unsigned int i = 0; i < steps; ++i) {
		do {
			generatorA = step(generatorA, 16807);
		} while (mode && generatorA & 3);
		do {
			generatorB = step(generatorB, 48271);
		} while (mode && generatorB & 7);

		if ((generatorA & 0xFFFF) == (generatorB & 0xFFFF)) {
			++count;
		}

		// dump first values
		if (i == 0) {
			printf("--Gen. A--  --Gen. B--\n");
		}
		if (i < 10) {
			int maxwidth = 10;
			printf("%*lu  %*lu\n", maxwidth, generatorA, maxwidth, generatorB);
		}
	}

	printf("\n");
	
	return count;
}

int main() {

	unsigned int count1 = iterate(40000000, false);
	unsigned int count2 = iterate(5000000, true);

	printf("Part One: %d match%s\n", count1, count1 > 1 ? "es" : "");
	printf("Part Two: %d match%s\n", count2, count2 > 1 ? "es" : "");
	printf("\n");

	return 0;
}
