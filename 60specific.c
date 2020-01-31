#include <stdio.h>
#include <stdlib.h>
#include <string.h>
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

    int *p = (int*)malloc(1000000 * sizeof(int));
    if (!p) {
        printf("mem did not alloc\n");
        return;
    }
    
    p[0] = 0; p[1] = 0;
    primes(p, 1000000);
    printf("%d\n", p[999999]);

    int sum = 100000, arr[5], i, j, tmp1, tmp2, sumsprime = 0;
    int alist[] = {3, 7, 11, 23, 269};
    int blist[] = {7, 17, 19, 23, 37, 311, 467, 617, 677};
    int clist[] = {67, 97, 109, 449, 541, 617, 677, 743, 827, 887};
    int dlist[] = {673, 827, 1871, 2069, 2377, 2741, 3727, 4159, 4253, 4507};
    int a, b, c, d, e, alen, blen, clen, dlen, *pa, *pb, *pc, *pd;
    alen = sizeof(alist) / sizeof(int);
    blen = sizeof(blist) / sizeof(int);
    clen = sizeof(clist) / sizeof(int);
    dlen = sizeof(dlist) / sizeof(int);

    for (a = 0, pa = alist; a < alen; a++, pa++)
        for (b = 0, pb = blist; b < blen; b++, pb++)
            for (c = 0, pc = clist; c < clen; c++, pc++)
                for (d = 0, pd = dlist; d < dlen; d++, pd++)
                    for (e = *pd+1; e < 100000; e++) {
                        if (!p[e]) continue;
                        //printf("%d %d %d %d %d\n", *pa, *pb, *pc, *pd, e);
                        arr[0] = *pa; arr[1] = *pb; arr[2] = *pc; arr[3] = *pd, arr[4] = e; 
                        sumsprime = 1;
                        for (i = 0; i < 4; i++) {
                            if (!sumsprime) break;
                            for (j = i + 1; j < 5; j++) {
                                tmp1 = join(arr[i], arr[j]);
                                tmp2 = join(arr[j], arr[i]);
                                //printf("tmp1 %d tmp2 %d ", tmp1, tmp2);
                                //printf("!p[tmp1] %d !p[tmp2] %d\n", !p[tmp1], !p[tmp2]);
                                //if (!p[tmp1] || !p[tmp2]) {
                                if (!isprime(tmp1) || !isprime(tmp2)) {
                                    sumsprime = 0;
                                    break;
                                }
                            }
                        }
                        if (sumsprime) {
                            sum = *pa + *pb + *pc + *pd + 3;
                            printf("a:%d b:%d c:%d d:%d e:%d sum:%d\n", *pa, *pb, *pc, *pd, e, sum);
                        }
                    }
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
