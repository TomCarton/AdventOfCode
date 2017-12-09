// instructions.c
//
// written by Thomas CARTON
//

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#include "instructions.h"


char *readInstructionsFile(const char *filename) {
	char *buffer = NULL;

	FILE *file = fopen(filename, "r");
	if (file) {
		fseek(file, 0, SEEK_END);
		unsigned int bufferSize = ftell(file);
		fseek(file, 0, SEEK_SET);

		buffer = malloc(bufferSize);

		fread(buffer, 1, bufferSize, file);

		fclose(file);
	}

	return buffer;
}

char *readLine(const char *buffer, char *line) {
	char *s = (char *)buffer, c;
	
	while ((c = *s++) && c != '\n');
	unsigned int len = s - buffer;

	strncpy(line, buffer, len - 1);
	line[len - 1] = 0;

	return c == '\n' ? s : NULL;
}

int getTokens(char *line, char **token, int maxTokens) {
	unsigned int t = 0;

	unsigned int mode = 0;
	for (unsigned int i = 0; i < 128; ++i) {
		char c = line[i];
		switch (mode) {
			case 0:
				if (c != ' ') {
					token[t] = (char *)&line[i];

					mode = 1;
				}
				break;

			case 1:
				if (c == ' ') {
					line[i] = 0;
					++t;

					mode = 0;
				}
				break;
		}
		if (c == '\n') {
			line[i] = 0;
			break;
		}
		if (t >= maxTokens) {
			break;
		}
	}

	return t + 1;
}