#include <stdio.h>
#include <stdlib.h>
#include "euler.h"

int join(int x, int y) {
    int tmp = y;
    while (y) {
        x *= 10;
        y /= 10;
    }
    return x + tmp;
}

int main(int argc, char **argv) {

    int sum = 100000, arr[5], i, j, tmp1, tmp2, sumsprime = 0;
    int *p = (int*)malloc(10000000 * sizeof(int));
    if (!p) {
        printf("mem did not alloc\n");
        return;
    }
    
    p[0] = 0; p[1] = 0;
    primes(p, 10000000);
    printf("%d\n", p[9999999]);

    int a, b, c, d, e;
    for (a = 2; a < 20; a++) {
        if (!p[a]) continue;
        for (b = a + 1; b < 50; b++) {
            if (!p[b]) continue;
            for (c = b + 1; c < 500; c++) {
                if (!p[c]) continue;
                for (d = c + 1; d < 1000; d++) {
                    if (!p[d]) continue;
                    for (e = d + 1; e < 5000; e++) {
                        if (!p[e]) continue;
                        //printf("%d %d %d %d %d\n", a, b, c, d, e);
                        arr[0] = a; arr[1] = b; arr[2] = c; arr[3] = d, arr[4] = e; 
                        sumsprime = 1;
                        for (i = 0; i < 4; i++) {
                            if (!sumsprime) break;
                            for (j = i + 1; j < 5; j++) {
                                tmp1 = join(arr[i], arr[j]);
                                tmp2 = join(arr[j], arr[i]);
                                //printf("tmp1 %d tmp2 %d ", tmp1, tmp2);
                                //printf("!p[tmp1] %d !p[tmp2] %d\n", !p[tmp1], !p[tmp2]);
                                if (!p[tmp1] || !p[tmp2]) {
                                    sumsprime = 0;
                                    break;
                                }
                            }
                        }
                        if (sumsprime && (a+b+c+d+e) < sum) {
                            sum = a+b+c+d+e;
                            printf("a:%d b:%d c:%d d:%d e:%d sum:%d\n", a, b, c, d, e, sum);
                        }}}}}}
    printf("%d\n", sum);
    printf("a:%d b:%d c:%d d:%d e:%d sum:%d\n", a, b, c, d, e, sum);
    return 0;
}

/*
3, 7, 109, and 673, are quite remarkable. By taking any two primes and
concatenating them in any order the result will always be prime. For example,
taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes,
792, represents the lowest sum for a set of four primes with this property.
Find the lowest sum for a set of five primes for which any two primes
concatenate to produce another prime.
*/