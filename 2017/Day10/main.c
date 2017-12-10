// Day 10
// Advent of Code 2017
//
// written by Thomas CARTON
//

#include <stdio.h>

#define kNodeCount 5

unsigned int Node[kNodeCount];
unsigned int Length[] = { 3, 4, 1, 5, };
// 94,84,0,79,2,27,81,1,123,93,218,23,103,255,254,243
unsigned int LengthCount = sizeof(Length) / sizeof(Length[0]);

unsigned int Curs;
unsigned int Skip = 0;

void initNodeList() {
	for (unsigned int i = 0; i < kNodeCount; ++i) {
		Node[i] = i;
	}
	Curs = 0;
}

void dumpNodeList(unsigned int length) {
	printf("LIST:");

	for (unsigned int i = 0; i < kNodeCount; ++i) {
		printf(" ");
		if (i == Curs) {
			if (length) { printf("("); }
			printf("[");
		}
		printf("%d", Node[i]);
		if (i == Curs) { printf("]"); }
		if (length && i == (Curs + length - 1) % kNodeCount) {
			printf(")");
		}
	}

	printf("\n");
}


void reverse(unsigned int length) {
	unsigned int Chunk[length];

	for (unsigned int i = 0; i < length; ++i) {
		Chunk[i] = Node[(Curs + length - i - 1) % kNodeCount];
	}

	// printf("CHUNK:");
	// for (unsigned int i = 0; i < length; ++i) {
	// 	printf(" %d", Chunk[i]);
	// }
	// printf("\n");

	for (unsigned int i = 0; i < length; ++i) {
		Node[(Curs + i) % kNodeCount] = Chunk[i];
	}	
}

int main() {
	initNodeList();
	dumpNodeList(0);

	for (unsigned int i = 0; i < LengthCount; ++i) {
		printf("\n\n-- %d\n", Length[i]);
		dumpNodeList(Length[i]);
		reverse(Length[i]);
		dumpNodeList(Length[i]);

		Curs = (Curs + Length[i] + Skip++) % kNodeCount;
	}

	printf("\n\n===============\n");
	dumpNodeList(0);
	printf("result 0 x 1: %d x %d = %d\n\n", Node[0], Node[1], Node[0] * Node[1]);
	return 0;
}