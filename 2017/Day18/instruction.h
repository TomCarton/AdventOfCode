// Day 18
// instruction.h
//
// written by Thomas CARTON
//

#ifndef __INSTRUCTION_H__
#define __INSTRUCTION_H__

char *getLine(const char *str, char *line);

typedef struct {
	char token[3][8];
} Instruction;

unsigned int getInstructions(const char *source, Instruction *instruction);
int runInstruction(Instruction *instruction);

#endif // __INSTRUCTION_H__
