// Day 18
// register.c
//
// written by Thomas CARTON
//

#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>

#include "../common/input.h"

#include "register.h"

#define IsNumeric(c) (((c) >= '0' && (c) <= '9') || c == '-' || c == '+' || c == '.')
#define IsAlpha(c) ((c) >= 'a' && (c) <= 'z')

typedef enum {
    kModeNone = 0,

    kModeNumeric,
    kModeAlpha,
} ValueMode;

long int Register[26];

void initRegisters() {
	for (unsigned int i = 0; i < 26; ++i) {
		Register[i] = 0;
	}
}

void dumpRegisters(unsigned int count) {
	printf("\n");

	for (unsigned int i = 0; i < count; ++i) {
		printf(" %c  ", 'a' + i);
	}
	printf("\n");

	for (unsigned int i = 0; i < count; ++i) {
		printf("----");
	}
	printf("\n");

	for (unsigned int i = 0; i < count; ++i) {
		printf("%03lu ", Register[i]);
	}
	printf("\n\n");
}

int value(const char *string) {

    int mode = 0;

    char *s = (char *)string, c;
    while ((c = *s)) {
        switch (mode) {
            case kModeNone:
                if (IsNumeric(c)) {
                    mode = kModeNumeric;
                    continue;
                } else if (IsAlpha(c)) {
                    mode = kModeAlpha;
                    continue;
                }
                break;

            case kModeNumeric:
                if (IsNumeric(c)) { ++s; continue; }
                break;

            case kModeAlpha:
                if (IsAlpha(c) && (s - string == 0)) { ++s; continue; }
                break;
        }

        mode = kModeNone;
        break;
    }

    if (mode == kModeNumeric) {
        int value;
        if (sscanf(string, "%d", &value) == 1) {
            return value;
        }

    } else if (mode == kModeAlpha) {
        return Register[s[-1] - 'a'];
    }


    fprintf(stderr, "!Unknown operand %s\n", string);
    return 0;
}
