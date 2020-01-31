#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void primes(short arr[], int upto) {
    int i, j;
    for (i = 2; i < upto; i++) arr[i] = 1;
    i = 2;
    j = i + i;
    while (i * i < upto) {
        while (j < upto) {
            arr[j] = 0;
            j += i;
        }
        i++;
        while (arr[i] == 0) i++;
        j = i + i;
    }
}

int join(int x, int y) {
    int tmp = y;
    while (y > 0) {
        x *= 10;
        y /= 10;
    }
    return x + tmp;
}

int main(int argc, char **argv) {

    int i, j, tmp1, tmp2, a, b, c, d, e, cnt = 0, ncnt = 0, sum = 1000000;
    short sumsprime;
    int arr[5] = {0,0,0,0,0};

    short *p = (short*)malloc(100000000 * sizeof(short));
    p[0] = 0;
    p[1] = 0;
    primes(p, 100000000);
    printf("%d\n", p[99999999]);

    for (i = 3; i < 10000; i++) if (p[i]) ncnt++;
    printf("ncnt is %d\n", ncnt);
    int n[ncnt]; // primes 3 to 10,000
    j = 0;
    for (i = 3; i < 10000; i++) {
        if (p[i]) {
            n[j] = i;
            j++;
        }
    }
    
    short **mem = malloc(10000 * sizeof(short*));
    for (i = 0; i < 10000; i++) {
    	mem[i] = malloc(10000 * sizeof(short));
        for (j = 0; j < 10000; j++) mem[i][j] = -1;
    }
    
    for (a = 0; a < ncnt; a++) {
        arr[0] = n[a];
        for (b = a + 1; b < ncnt; b++) {
            arr[1] = n[b];
            for (c = b + 1; c < ncnt; c++) {
                arr[2] = n[c];
                for (d = c + 1; d < ncnt; d++) {
                    arr[3] = n[d];
                    sumsprime = 1;
                    for (i = 0; i < 3; i++) {
                        if (sumsprime == 0) break;
                        for (j = i + 1; j < 4; j++) {
                            if (mem[arr[i]][arr[j]] == 0) {
                                sumsprime = 0;
                                break;
                            }
                            else if (mem[arr[i]][arr[j]] == 1) continue;
                            else {
                                tmp1 = join(arr[i], arr[j]);
                                tmp2 = join(arr[j], arr[i]);
                                if (p[tmp1] == 0 || p[tmp2] == 0) {
                                    mem[arr[i]][arr[j]] = 0;
                                    sumsprime = 0;
                                    break;
                                }
                                mem[arr[i]][arr[j]] = 1;
                            }
                        }
                    }
                    if (sumsprime == 1) {
                        sum = 0;
                        for (i = 0; i < sizeof(arr)/4; i++) {
                            sum += arr[i];
                            printf("%d ", arr[i]);
                        }
                        printf("%d\n", sum);
                    }
                }
            }
        }
    }
}

//3, 7, 109, and 673, are quite remarkable. By taking any two primes and
//concatenating them in any order the result will always be prime. For example,
//taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes,
//792, represents the lowest sum for a set of four primes with this property.
//Find the lowest sum for a set of five primes for which any two primes
//concatenate to produce another prime.
