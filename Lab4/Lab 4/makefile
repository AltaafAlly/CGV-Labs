# Makefile for lab4.c

# Compiler
CC = gcc

# Compiler flags
CFLAGS = -Wall

# Libraries
LIBS = -lGL -lglut

# Source file
SRC = lab4.c

# Output binary
OUT = lab4

all: $(OUT)

$(OUT): $(SRC)
	$(CC) $(CFLAGS) $(SRC) -o $(OUT) $(LIBS)

clean:
	rm -f $(OUT)

.PHONY: all clean
