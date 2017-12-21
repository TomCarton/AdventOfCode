# Makefile

TARGET := day20

C_FILES := $(wildcard *.c) $(wildcard ../common/*.c)

CC=clang
CC_FLAGS=-Wall -Werror -O3 -g

all: $(C_FILES)
	$(CC) $(CC_FLAGS) $^ -o $(TARGET)

.PHONY: clean
clean:
	rm $(TARGET)

.PHONY: info
info:
	@echo sources: $(C_FILES)
	@echo objects: $(OBJ_FILES)
