// input.c
//
// written by Thomas CARTON
//

#include <stdlib.h>
#include <stdio.h>

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
			buffer = malloc(bufferSize);
			if (buffer) {
				read = fread(buffer, 1, bufferSize, file);
			}
		}

		fclose(file);
	}

	*data = buffer;

	return read;
}
