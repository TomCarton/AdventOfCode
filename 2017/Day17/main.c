// Day 17
//
// written by Thomas CARTON
//

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

// static const unsigned int kSpinAmount = 2017 + 1;
static const unsigned int kSpinAmount = 50000000 + 1;

unsigned int Buffer[kSpinAmount + 1];

unsigned int BufferPosition = 0;
unsigned int BufferSize = 0;

unsigned int Input = 345;

void dump() {
	for (unsigned int i = 0; i < BufferSize; ++i) {
		if (i == BufferPosition) {
			printf("(%d) ", Buffer[i]);
		} else {
			printf("%d ", Buffer[i]);
		}
		if (i && (i % 20 == 0)) printf("\n");
	}

	printf("\n");
}

int main() {
	memset(Buffer, 0, kSpinAmount * sizeof(Buffer[0]));

	BufferPosition = 0;
	BufferSize = 1;

	for (unsigned int v = 1; v < kSpinAmount; ++v) {
		if ((v & 0xFF) == 0) printf("\rspin %d -> %0.2f", v, 100.f * v / kSpinAmount);
		BufferPosition = ((BufferPosition + Input) % BufferSize++) + 1;
		for (unsigned int i = BufferSize - 2; i >= BufferPosition; --i) {
			Buffer[i + 1] = Buffer[i];
		}
		Buffer[BufferPosition] = v;
	}
	
	// dump();
	printf("\r");
	printf("pos: %d, size: %d\n", BufferPosition, BufferSize);
	printf("result: %d\n", Buffer[(BufferPosition + 1) % BufferSize]);

	return 0;
}
