// Day01
//
// written by Thomas CARTON
//

#include <stdio.h>
#include <stdlib.h>

char *Input = NULL;
unsigned int InputSize = 0;

unsigned int readInput(const char *filename) {
	unsigned int read = 0;

	FILE *file = fopen(filename, "r");
	if (file) {
		fseek(file, 0, SEEK_END);
		InputSize = ftell(file);
		fseek(file, 0, SEEK_SET);

		Input = malloc(InputSize);

		read = fread(Input, 1, InputSize, file);

		fclose(file);
	}

	return read;
}

int main() {
	readInput("input.txt");

	int floor = 0;
	int basement = 0;
	for (unsigned int i = 0; i < InputSize; ++i) {
		char c = Input[i];
		
		switch (c) {
			case '(':
				++floor;
				break;
			case ')':
				--floor;
				break;		
		}

		if (floor < 0 && basement == 0) {
			basement = i + 1;
		}
	}

	printf("Floor: %d\n", floor);
	printf(" basement inst = %d\n", basement);

	return 0;
}
