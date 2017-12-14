// main.c
//
// written by Thomas CARTON
//

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#include "knot.h"

char Input[] = "uugsqrei";

char *keyForRow(unsigned int row) {
	char *key = malloc(strlen(Input) + 10);

	sprintf(key, "%s-%d", Input, row);

	key[strlen(key) + 0] = 17;
	key[strlen(key) + 1] = 31;
	key[strlen(key) + 2] = 73;
	key[strlen(key) + 3] = 47;
	key[strlen(key) + 4] = 23;
	key[strlen(key) + 5] = '\0';

	return key;
}

int main() {

	for (unsigned int row = 0; row < 128; ++row) {

		char *key = keyForRow(row);

		printf("%16s: ", key);

		hash(key);

		free(key);
	}

	return 0;
}
