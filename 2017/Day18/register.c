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
	for (unsigned int j = 0; j < count / 8; ++ j) {
		unsigned int width = count - j * 8;
		if (width > 8) width = 8;

		for (unsigned int i = 8 * j; i < 8 * j + width; ++i) {
			printf("| %c = %010lu ", 'a' + i, Register[i]);
		}

		printf("|\n");
	}
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
