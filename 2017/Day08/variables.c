// variables.c
//
// written by Thomas CARTON
//

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#include "variables.h"

VAR *Variable = NULL;
unsigned int VariableSpace = 0;
unsigned int VariableCount = 0;

VAR *addVariable(const char *label) {

	if (Variable == NULL) {
		VariableSpace = 8;
		Variable = malloc(VariableSpace * sizeof(VAR));
	}
	if (VariableCount + 1 > VariableSpace) {
		VAR *vars = malloc(2 * VariableSpace * sizeof(VAR));
		memcpy(vars, Variable, VariableSpace * sizeof(VAR));
		free(Variable);
		Variable = vars;
		VariableSpace *= 2;
	}

	VAR *var = &Variable[VariableCount];
	strcpy(var->label, label);
	var->value = 0;

	++VariableCount;

	return var;
}

VAR *getVariable(const char *label) {
		
	for (unsigned int i = 0; i < VariableCount; ++i) {
		if (strcmp(Variable[i].label, label) == 0) {
			return &Variable[i];
		}
	}

	return addVariable(label);
}

void dumpVariable(const VAR *var)
{
	printf(" '%s' = %d\n", var->label, var->value);
}

void dumpVariables(void)
{
	int max = 0;
	printf("\n------------------------\n");
	for (unsigned int i = 0; i < VariableCount; ++i) {
		printf("%2d: '%s' = %d\n", i, Variable[i].label, Variable[i].value);

		if (Variable[i].value > max) {
			max = Variable[i].value;
		}
	}
	printf("------------------------\n");
	printf("Max value = %d\n", max);
	printf("------------------------\n\n");
}
