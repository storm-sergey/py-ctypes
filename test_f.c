#include <stdio.h>
#include <wchar.h>


double foo1(short i) {
   return(double)i;
}

const wchar_t* foo2(const wchar_t* s) {
   const wchar_t* test_s = s;
   return test_s;
}

void* foo3(double d, int l, const wchar_t* s) {
   printf("\"first param\"=%f, \"second param\"=%d, ", d, l);
   wprintf(L"\"third param\"=\"%ls\"\n", s);
   return(void*)s;
}

void foo4(int rows, int array[rows]) {
    printf("%d \n", rows);
    for (int i = 0; i < rows; i++) {
        printf("%d ", array[i]);
    }
}
