// variables.h
//
// written by Thomas CARTON
//

typedef struct {
	char label[16];
	int value;
} VAR;

VAR *addVariable(const char *label);
VAR *getVariable(const char *label);

void dumpVariable(const VAR *var);
void dumpVariables(void);
