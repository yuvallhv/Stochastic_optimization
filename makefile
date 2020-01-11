all: patience_sorting

patience_sorting: patience_sorting.o
	gcc -g -Wall -o patience_sorting patience_sorting.o

# Depends on the source and header files
patience_sorting.o: patience_sorting.c
	gcc -g -Wall -c -o patience_sorting.o patience_sorting.c

#tell make that "clean" is not a file name!
.PHONY: clean

#Clean the build directory
clean: 
	rm -f *.o main
