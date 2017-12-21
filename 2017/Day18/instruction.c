// Day 18
// instruction.c
//
// written by Thomas CARTON
//

#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>

#include "../common/input.h"

#include "register.h"

#include "instruction.h"

static const unsigned int kLineMaxLength = 32;

#define isBlank(c) (((c) == ' ') || ((c) == '\t'))
#define isEndLine(c) (((c) == '\n') || ((c) == '\0'))

char *getLine(const char *str, char *line) {
	char *s = (char *)str, c;
	
	while ((c = *s++) && isBlank(c));
	char *start = s - 1;

	while ((c = *s++) && !isEndLine(c));
	char *end = s;

	unsigned int size = end - start - 1;
	if (size < 1) {
		return NULL;
	}
	if (size > kLineMaxLength) {
		size = kLineMaxLength;
	}

	strncpy(line, start, size);
	line[size] = '\0';

	return s;
}

unsigned int getInstructions(const char *source, Instruction *instruction) {
	unsigned int count = 0;
	char line[kLineMaxLength + 1];

	char *s = (char *)source;
 	while ((s = getLine(s, line))) {
 		if (line[0] == '#') continue;
 		if (line[0] == '\0') break;

		if (instruction) {
			unsigned int t = 0;
 			char *token;
			char *str = line;
 			while ((token = strsep(&str, " \t")) != NULL) {
 				strcpy(instruction[count].token[t++], token);
 			}
 		}

 		++count;
	}

	return count;
}

int frequency = 0;

int runInstruction(Instruction *instruction) {
	// set
	if (strcmp(instruction->token[0], "set") == 0) {
		if (strlen(instruction->token[1]) == 1) {
			Register[instruction->token[1][0] - 'a'] = value(instruction->token[2]);
		}
	// add
	} else if (strcmp(instruction->token[0], "add") == 0) {
		if (strlen(instruction->token[1]) == 1) {
			Register[instruction->token[1][0] - 'a'] += value(instruction->token[2]);
		}
	// mul
	} else if (strcmp(instruction->token[0], "mul") == 0) {
		if (strlen(instruction->token[1]) == 1) {
			Register[instruction->token[1][0] - 'a'] *= value(instruction->token[2]);
		}
	// mod
	} else if (strcmp(instruction->token[0], "mod") == 0) {
		if (strlen(instruction->token[1]) == 1) {
			Register[instruction->token[1][0] - 'a'] %= value(instruction->token[2]);
		}
	// snd
	} else if (strcmp(instruction->token[0], "snd") == 0) {
		frequency = value(instruction->token[1]);
	// rcv
	} else if (strcmp(instruction->token[0], "rcv") == 0) {
		if (value(instruction->token[1]) != 0) {
			printf("\nRecover frequency of %d\n\n", frequency);
			return 0;
		}
	// jgz
	} else if (strcmp(instruction->token[0], "jgz") == 0) {
		if (value(instruction->token[1]) > 0) {
			return value(instruction->token[2]);
		}
	}

	return 1;
}
