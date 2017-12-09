// main.c
//
// written by Thomas CARTON
//

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#include "instructions.h"

static unsigned int kMaxTokens = 8;

int main() {

	char *lines = readInstructionsFile("instructions.txt");

	char line[128] = "\0";

	while ((lines = readLine(lines, line))) {
		printf("line: '%s'\n", line);

		char *token[kMaxTokens];
		for (unsigned int i = 0; i < kMaxTokens; ++i) {
			token[i] = NULL;
		}

		int t = getTokens(line , token, kMaxTokens);
		printf(" token %d\n", t);

		for (unsigned int i = 0; i < t; ++i) {
			printf("token %d = '%s'\n", i, token[i]);
		}

		printf("\n");
	}

	return 0;
}
