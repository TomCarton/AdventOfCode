// Day 17 - part 2
//
// written by Thomas CARTON
//

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

static const unsigned int kSpinAmount = 50000000;
static const unsigned int kInput = 345;

int main() {
    unsigned int bufferSize = 1;
    
    unsigned int result = 0;
    unsigned int pos = 0;

    for (unsigned int i = 1; i <= kSpinAmount; ++i, ++pos) {
        if ((pos = (pos + kInput) % bufferSize++) == 0) {
        	result = i;
        }
    }

	printf("Part 2 = %d\n", result);

	return 0;
}
