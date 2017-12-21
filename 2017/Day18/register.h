// Day 18
// register.h
//
// written by Thomas CARTON
//

#ifndef __REGISTER_H__
#define __REGISTER_H__

extern long int Register[26];

void initRegisters();
void dumpRegisters(unsigned int count);

int value(const char *string);

#endif // __REGISTER_H__
