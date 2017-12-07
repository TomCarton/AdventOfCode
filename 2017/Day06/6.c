// Day 6
//
// written by Thomas CARTON
//

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>


int bank[] = { 5, 1, 10, 0, 1, 7, 13, 14, 3, 12, 8, 10, 7, 12, 0, 6, };
// int bank[] = { 0, 2, 7, 0, };
int bankCount;

void dumpBank(int *bank) {
    for (unsigned int i = 0; i < bankCount; ++i) {
        printf("%d\t", bank[i]);
    }
    printf("\n");
}

int *history = NULL;
int historyCount = 0;

void saveHistory(int *bank) {
    if (history == NULL) {
        history = malloc(sizeof(bank) * 256);
    }

    memcpy(history + historyCount * bankCount, bank, sizeof(int) * bankCount);
    ++historyCount;
}

bool isHistory(int *bank) {
    for (unsigned int i = 0; i < historyCount; ++i) {
        int *savedBank = &history[i * bankCount];
        if (memcmp(bank, savedBank, sizeof(int) * bankCount) == 0) {
            return true;
        }
    }

    return false;
}

void dispatchBank(int *bank) {
    int max = 0;
    unsigned int maxi = 0;
    for (unsigned int i = 0; i < bankCount; ++i) {
        if (bank[i] > max) {
            max = bank[i];
            maxi = i;
        }
    }

    bank[maxi] = 0;
    unsigned int i = maxi + 1;
    while (max--) {
        i %= bankCount;

        ++bank[i++];
    }
}

int main(int argc, const char * argv[]) {

    bankCount = sizeof(bank) / sizeof(bank[0]);
	int iter = 0;
   	
   	printf("%d:\t", iter++);
	dumpBank(bank);
    
    do {
        saveHistory(bank);
        dispatchBank(bank);

        printf("%d:\t", iter++);
        dumpBank(bank);
    } while (isHistory(bank) == false);

    return 0;
}

