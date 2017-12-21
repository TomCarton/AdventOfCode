// input.c
//
// written by Thomas CARTON
//

#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <string.h>

const unsigned int kLineMaxLength = 128;

#define isBlank(c) (((c) == ' ') || ((c) == '\t'))
#define isEndLine(c) (((c) == '\n') || ((c) == '\0'))

unsigned int readInput(const char *filename, char **data) {
	unsigned int read = 0;
	unsigned int bufferSize = 0;
	char *buffer = NULL;

	FILE *file = fopen(filename, "r");

	if (file) {
		fseek(file, 0, SEEK_END);
		bufferSize = ftell(file);
		fseek(file, 0, SEEK_SET);

		if (bufferSize) {
			buffer = malloc(bufferSize + 1);
			if (buffer) {
				read = fread(buffer, 1, bufferSize, file);
				buffer[bufferSize] = 0;
			}
		}

		fclose(file);
	}

	*data = buffer;

	return read;
}

bool getLine(char **str, char *line) {
	char *s = (char *)*str, c;
	
	while ((c = *s++) && isBlank(c));
	char *start = s - 1;

	while ((c = *s++) && !isEndLine(c));
	char *end = s;

	*str = s;

	unsigned int size = end - start - 1;
	if (size <= 1) {
		return false;
	}
	if (size > kLineMaxLength) {
		size = kLineMaxLength;
	}

	if (line) {
		strncpy(line, start, size);
		line[size] = '\0';
	}

	return true;
}
