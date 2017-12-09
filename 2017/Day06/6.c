// Day 6
//
// written by Thomas CARTON
//

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>


// int bank[] = { 0, 2, 7, 0, };
int Bank[] = { 5, 1, 10, 0, 1, 7, 13, 14, 3, 12, 8, 10, 7, 12, 0, 6, };
int BankCount;

void dumpBank(int *bank) {
    for (unsigned int i = 0; i < BankCount; ++i) {
        printf("%d\t", Bank[i]);
    }
    printf("\n");
}

int *History = NULL;
int HistorySpace = 0;
int HistoryCount = 0;

void saveHistory(int *bank) {
    if (History == NULL) {
        HistorySpace = 8;
        History = malloc(sizeof(Bank) * HistorySpace);
    }
    if (HistoryCount + 1 >= HistorySpace) {
        int *h = malloc(2 * HistorySpace * sizeof(Bank));
        memcpy(h, History, HistorySpace * sizeof(Bank));
        free(History);
        History = h;
        HistorySpace *= 2;
    }
    
    memcpy(History + HistoryCount * BankCount, bank, sizeof(Bank));
    ++HistoryCount;
}

bool isHistory(int *bank) {
    for (unsigned int i = 0; i < HistoryCount; ++i) {
        int *savedBank = &History[i * BankCount];
        if (memcmp(bank, savedBank, sizeof(Bank)) == 0) {
            printf("loop count = %d\n", HistoryCount - i);
            return true;
        }
    }
    
    return false;
}

void dispatchBank(int *bank) {
    int max = 0;
    unsigned int maxi = 0;
    for (unsigned int i = 0; i < BankCount; ++i) {
        if (bank[i] > max) {
            max = bank[i];
            maxi = i;
        }
    }
    
    bank[maxi] = 0;
    unsigned int i = maxi + 1;
    while (max--) {
        i %= BankCount;
        
        ++bank[i++];
    }
}

int main(int argc, const char * argv[]) {
    
    BankCount = sizeof(Bank) / sizeof(Bank[0]);
    int iter = 0;
    
    printf("%d:\t", iter++);
    dumpBank(Bank);
    
    do {
        saveHistory(Bank);
        dispatchBank(Bank);
        
        printf("%d:\t", iter++);
        dumpBank(Bank);
    } while (isHistory(Bank) == false);
    
    free(History);
    
    return 0;
}
