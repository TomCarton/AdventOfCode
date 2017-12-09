// instructions.h
//
// written by Thomas CARTON
//

char *readInstructionsFile(const char *filename);
char *readLine(const char *buffer, char *line);
int getTokens(char *line, char **token, int maxTokens);
