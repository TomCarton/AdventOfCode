// Day 18
//
// written by Thomas CARTON
//

#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>

#include "../common/input.h"

#include "source.h"
#include "register.h"

#define DEBUG 1

void clearScreen(void) {
	printf("\033[H\033[J");
}

int main() {
    char *source = NULL;
	readInput("input.txt", &source);

	unsigned int instructionCount = getInstructions(source, NULL);
	Instruction *instruction = malloc(instructionCount * sizeof(Instruction));
	getInstructions(source, instruction);

	initRegisters();

	int pc = 0, inc = 1;
	while (pc < instructionCount && inc) {

#		if DEBUG
			clearScreen();
			dumpRegisters(17);
			
			printf("\ninstruction: %02d - %s", pc, instruction[pc].token[0]);
			if (instruction[pc].token[1]) printf(" %s", instruction[pc].token[1]);
			if (instruction[pc].token[2]) printf(" %s", instruction[pc].token[2]);
			printf("\n");

			getchar();
#		endif

		inc = runInstruction(&instruction[pc]);
		pc += inc;
	}

	free(instruction);

	free(source);

	return 0;
}
