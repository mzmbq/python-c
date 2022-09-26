.PHONY: build

# source: https://stackoverflow.com/questions/5081875/ctypes-beginner
build:
	gcc -shared -O3 -Wl,-soname,testlib -o bin/testlib.so -fPIC lib/lib.c