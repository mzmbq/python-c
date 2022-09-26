#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

void hello() 
{
    printf("Hello\n");
}

void cfun(const double *indatav, size_t size, double *outdatav) 
{
    size_t i;
    for (i = 0; i < size; ++i)
        outdatav[i] = indatav[i] * 2.0;
}


uint32_t* foo(const uint32_t* key_can, int m, int n, uint32_t* result)
{
    int length = 65000;
    for (int i = 0; i < length; i++) {
        // TODO: implement
    }
}