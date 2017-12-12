// Day 12
//
// written by Thomas CARTON
//

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

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

typedef struct {
	unsigned int count;
	unsigned int pipe[32];
} PROGRAM;

#define kProgCount 2000
PROGRAM prog[kProgCount];

void dumpPrograms() {
	for (unsigned int pid = 0; pid < kProgCount; ++pid) {
		printf("%d <-> ", pid);
		for (unsigned int i = 0; i < prog[pid].count; ++i) {
			printf("%d%s", prog[pid].pipe[i], i < prog[pid].count - 1 ? ", " : "\n");
		}
	}
}

void parse(const char *buffer, unsigned int size) {
	
	unsigned int mode = 0;
	unsigned int pid, pipidx, pipid;

	char *s = (char *)buffer, c;
	while ((c = *s++) && (s - buffer < size)) {
		switch (mode) {
			case 0:
				pid = 0;
				pipidx = 0;
				pipid = 0;
				
				++mode;

			case 1:
				if (c >= '0' && c <= '9') {
					pid = pid * 10 + c - '0';
					break;
				}

				++mode;

			case 2:
				if (c == '<' && s[0] == '-' && s[1] == '>') {
					s += 2;
					++mode;
				} else break;

			case 3:
				if (c >= '0' && c <= '9') {
					pipid = pipid * 10 + c - '0';
				} else if (c == ',' || c == '\n') {
					prog[pid].pipe[pipidx++] = pipid;
					prog[pid].count = pipidx;
					pipid = 0;
				}

				if (c == '\n') {
					mode = 0;
				}
		}
	}

}

unsigned int parc[kProgCount];

void reset() {
	for (unsigned int i = 0; i < kProgCount; ++i) {
		parc[i] = 0;
	}
}

void step(unsigned int idx) {
	printf("step %d\n", idx);

	parc[idx] = 1;

	for (unsigned int i = 0; i < prog[idx].count; ++i) {
		unsigned int id = prog[idx].pipe[i];
		if (parc[id] == 0) {
			step(id);
		}
	}
}

unsigned int parcours(unsigned int start) {
	reset();
	step(start);

	unsigned int count = 0;
	for (unsigned int i = 0; i < kProgCount; ++i) {
		count += parc[i];
	}

	return count;
}

unsigned int groupCount() {
	unsigned int count = 0;
	reset();

	unsigned int i;
	do {
		for (i = 0; i < kProgCount; ++i) {
			if (parc[i] == 0) {
				++count;
				step(i);
				break;
			}
		}
	} while (i < kProgCount);

	return count - 1;
}

int main() {

	char *data = NULL;
	unsigned int read = readInput("input.txt", &data);

	parse(data, read);
	free(data);

	dumpPrograms();	

	printf("\ncount from '0' = %d (%d groups)\n", parcours(0), groupCount());

	return 0;
}