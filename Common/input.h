// input.h
//
// written by Thomas CARTON
//

extern const unsigned int kLineMaxLength;

unsigned int readInput(const char *filename, char **data);

bool getLine(char **str, char *line);
