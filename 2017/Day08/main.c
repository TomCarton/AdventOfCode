// main.c
//
// written by Thomas CARTON
//

#include <stdlib.h>
#include <stdio.h>

#include "instructions.h"
#include "variables.h"

int main() {

	int maxValue = 0;

	char *lines = readInstructionsFile("instructions.txt");

	char line[128] = "\0";
	while ((lines = readLine(lines, line))) {
		printf("line: '%s'\n", line);

		int value = runLine(line);
		if (value > maxValue) {
			maxValue = value;
		}
	}

	dumpVariables();

	printf("Max value during the process = %d\n\n", maxValue);

	return 0;
}
