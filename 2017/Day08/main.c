// main.c
//
// written by Thomas CARTON
//

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

#include "instructions.h"
#include "variables.h"

static unsigned int kMaxTokens = 8;

int main() {

	char *lines = readInstructionsFile("instructions.txt");

	char line[128] = "\0";

	while ((lines = readLine(lines, line))) {
		printf("line: '%s'\n", line);

		char *token[kMaxTokens];
		getTokens(line , token, kMaxTokens);

		bool result = true;
		if (strcmp(token[3], "if") == 0) {
			VAR *tVariable = getVariable(token[4]);
			int tValue = 0;
			sscanf(token[6], "%d", &tValue);

			if (strcmp(token[5], "<") == 0) {
				result = tVariable->value < tValue;
			} else if (strcmp(token[5], "<=") == 0) {
				result = tVariable->value <= tValue;
			} else if (strcmp(token[5], ">") == 0) {
				result = tVariable->value > tValue;
			} else if (strcmp(token[5], ">=") == 0) {
				result = tVariable->value >= tValue;
			}
		}

		VAR *var = getVariable(token[0]);

		if (result) {
			int dValue = 0;
			sscanf(token[2], "%d", &dValue);

			if (strcmp(token[1], "inc") == 0) {
				var->value += dValue;
			} else if (strcmp(token[1], "dec") == 0) {
				var->value -= dValue;
			}
		}
	}

	dumpVariables();

	return 0;
}
