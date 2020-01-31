#include <stdio.h>
#include <stdlib.h>
#include "euler.h"

int main(int argc, char **argv) {

    int *p = (int*)malloc(1000000 * sizeof(int));
    if (p == NULL) {
        printf("mem did not alloc\n");
        return;
    }
    p[0] = 0; p[1] = 0;
    primes(p, 1000000);
    //printf("%d\n", p[999999]);
    int cnt, tmp;
    char a[] = "0123456789";
    char b[] = "13579";
    char *pa, *pb, *pc, *pd, *pe, *pf, *pg, *px;
    for (pa = a; *pa; pa++)
        for (pb = a; *pb; pb++)
            //for (pc = a; *pc; pc++)
                //for (pd = a; *pd; pd++)
                    for (pf = b; *pf; pf++) {
                        cnt = 0;
                        for (px = a; *px; px++) {
                            tmp = (*px-'0') * 100000 + \
                                  (*pa-'0') * 10000 + \
                                  (*px-'0') * 1000 + \
                                  (*pb-'0') * 100 + \
                                  (*px-'0') * 10 + \
                                  (*pf-'0');
                            if (tmp < 100000) continue;
                            if (p[tmp]) {
                                cnt++;
                                if (*pa=='2' && *pb=='3' && *pf=='3') printf("%d ", tmp);
                            }
                        }
                        if (cnt > 7) printf("%d\n", tmp); 
                    }
    return 0;
}

/* By replacing the 1st digit of *3, it turns out that six of the nine possible
values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit
number is the first example having seven primes among the ten generated
numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and
56993. Consequently 56003, being the first member of this family, is the
smallest prime with this property.

Find the smallest prime which, by replacing part of the number, not necessarily
adjacent digits, with the same digit, is part of an eight prime value family.
*/
