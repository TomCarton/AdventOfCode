// Day 4
//
// written by Thomas CARTON
//

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main() {

	int size = 0, read;
	char *buffer;

	FILE *file = fopen("passphrases.txt", "r");
	if (file) {
		fseek(file, 0, SEEK_END);
		size = ftell(file);
		fseek(file, 0, SEEK_SET);

		buffer = malloc(size);
		read = fread(buffer, 1, size, file);

		fclose(file);
	}

	printf("size = %d\n", size);
	printf("read = %d\n", read);

	// printf("\n\n%s\n\n", buffer);

	char word[32][32];

	unsigned int correct = 0;
	if (read > 0) {

		char *s = buffer, c;
		char *sw = s;

		unsigned int l = 0;
		do {
			unsigned int w = 0;

			do {
				c = *s++;
				if (c == 0 || c == ' ' || c == '\n') {
					s[-1] = 0;
					strcpy(word[w++], sw);
					sw = s;
				}
			} while (c && c != '\n');

			printf("line %d: %d word%s (", ++l, w, w > 1 ? "s" : "");
			for (unsigned int i = 0; i < w; ++i) {
				printf("%s%s", word[i], i == w - 1 ? ")\n" : ", ");
			}

			int unik = 1;
			for (unsigned int i = 0; i < w - 1; ++i) {
				for (unsigned int j = i + 1; j < w; ++j)
				{
					if (strcmp(word[i], word[j]) == 0) {
						unik = 0;
						break;
					}
				}
			}
			if (unik) {
				++correct;
			}

		} while (s - buffer < size);
	}

	printf("correct = %d\n", correct);

	free(buffer);

	return 0;
}