// Day 5
//
// written by Thomas CARTON
//

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

char *buffer;
unsigned int fsize;
int *maze;
int lcount = 1;

void readFile() {
	FILE *file = fopen("maze.txt", "r");
	fseek(file, 0, SEEK_END);
	fsize = ftell(file);
	fseek(file, 0, SEEK_SET);

	printf("file size = %d\n", fsize);

	buffer = malloc(fsize);
	fread(buffer, 1, fsize, file);

	fclose(file);
}

void setMaze() {
	char *s = buffer, c;
	do {
		c = *s++;
		if (c == '\n') {
			++lcount;
		}
	} while (s - buffer < fsize);

	printf("%d line%s\n", lcount, lcount > 1 ? "s" : "");

	maze = malloc(lcount * sizeof(int));

	int p = 0;

	s = buffer;
	do {		
		char *st = s;
		int v = 0;
		sscanf(s, "%d\n", &v);

		maze[p++] = v;
		printf("found %d\n", v);

		while ((c = *s++) && c != '\n');
	} while (c);
}

int main() {

	readFile();
	setMaze();

	int steps = 0;

	int curs = 0;
	do {
		++steps;
		printf("step %6d: %04d %d\n", steps, curs, maze[curs]);
		int ex = curs;
		curs += maze[curs];
		++maze[ex];
	} while (curs > 0 && curs = lcount);

	return 0;
}