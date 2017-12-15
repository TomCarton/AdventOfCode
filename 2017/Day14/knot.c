// knot.c
//
// written by Thomas CARTON
//

#include <stdio.h>

#include "knot.h"


#define kNodeCount 256

unsigned int Node[kNodeCount];


void initNodeList() {
	for (unsigned int i = 0; i < kNodeCount; ++i) {
		Node[i] = i;
	}
}

void reverse(unsigned int cursor, unsigned int length) {
	unsigned int chunk[length];

	for (unsigned int i = 0; i < length; ++i) {
		chunk[i] = Node[(cursor + length - i - 1) % kNodeCount];
	}

	for (unsigned int i = 0; i < length; ++i) {
		Node[(cursor + i) % kNodeCount] = chunk[i];
	}	
}

void hash(const char *key) {
	initNodeList();

	int cursor = 0, skip = 0;
	for (unsigned int i = 0; i < 64; ++i) {
		unsigned int index = 0;
		while (key[index]) {
			unsigned int len = key[index];
			reverse(cursor, len);
			cursor = (cursor + len + skip) % kNodeCount;
			++skip;
			++index;
		}
	}

	char hash[256]; char *h = hash;
	for (unsigned int j = 0; j < 16; ++j) {
		int dense = Node[16 * j];
		for (unsigned int i = 1; i < 16; ++i) {
			dense ^= Node[16 * j + i];
		}
		sprintf(h, "%08X", dense);
		h += 8;
	}
	*h = '\0';

	printf("hash: %s\n", hash);
}

// stringstream hash_builder;
//         for (int i = 0; i < 16; ++i) {
//             int dense = list[16 * i];
//             for (int j = 1; j < 16; ++j)
//                 dense ^= list[16 * i + j];
//             hash_builder << hex << dense;
//         }
//         string hash = hash_builder.str();
//         for (char c : hash) {
//             res += count(c);
// }
