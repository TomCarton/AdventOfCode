// Day 18
// source.h
//
// written by Thomas CARTON
//

#ifndef __SOURCE_H__
#define __SOURCE_H__

char *getLine(const char *str, char *line);

typedef struct {
	char token[3][8];
} Instruction;

unsigned int getInstructions(const char *source, Instruction *instruction);
int runInstruction(Instruction *instruction);

#endif // __SOURCE_H__
