#include <stdio.h>
#include "euler.h"

int primes[10000] = {0, 0};
int i, j, k, arr1[4], arr3[4], n, done = 0, x;

void sort(int a[]) {
    int i, j, tmp;
    for (i = 0; i < 3; i++)
        for (j = i +1; j < 4; j++)
            if (a[j] > a[i]) {
                tmp = a[i];
                a[i] = a[j];
                a[j] = tmp;
            }
}

void intToArr(int n) {
    for (j = 3; j >= 0; j--) {
        arr1[j] = n % 10;
        n -= arr1[j];
        n /= 10;
    }
    arr1[j] = n;
}

int arrToInt(int arr[]) {
    n = 0;
    for (j = 0; j < 3; j++) {
        n += arr[j];
        n *= 10;
    }
    n += arr[j];
    return n;
}

int arrCmp(int a[], int b[]) {
    int i, tmp[4];
    for (i = 0; i < 4; i++) tmp[i] = a[i];
    sort(tmp); sort(b);
    if (tmp[0]==b[0] && tmp[1]==b[1] && tmp[2]==b[2] && tmp[3]==b[3])
        return 1;
    else
        return 0;
}

void printArr(int a[]) {
    int i;
    for (i = 0; i < 4; i++) {
        printf("%d", a[i]);
    }
}

int main(int argc, char **argv)  {

    for (i = 2; i < 10000; i++) primes[i] = 1;
    i = 2;
    j = i + i;
    while (i < 100) {
        // printf("i is %d j is %d\n", i, j);
        while (j < 10000) {
            primes[j] = 0;
            j += i;
        }
        i++;
        while (primes[i] == 0) i++;
        j = i + i;
    }

    for (i = 1488; i < 10000; i++) {
        if (primes[i]) {
            printf("\n%d is prime", i);
            intToArr(i);
            int arr2[4];
            for (k = 0; k < 4; k++) arr2[k] = arr1[k];
            do {
                nextPerm(arr1);
                printf("\n nextPerm is ");
                printArr(arr1);
                n = arrToInt(arr1);
                if (n < i) break;
                printf(" n is %d", n);
                if (primes[n])
                    if (n+n-i < 10000)    
                        if (primes[n+n-i]) {
                            x = n + n -i;
                            for (k = 3; k >= 0; k--) {
                                arr3[k] = x % 10;
                                x -= arr3[k];
                                x /= 10;
                            }
                            arr3[k] = x;
                            printf(" arr3 is "); printArr(arr3);
                            if (arrCmp(arr2, arr3)) {
                                printf(" answer is %d, %d, %d\n", i, n, n+n-i);
                                done = 1;
                                break;
                            }
                        }
            } while (n < 9000);
        }
        if (done) break;
    }
    return 0;
}

/* The arithmetic sequence 1487, 4817, 8147, in which each of the terms
increases by 3330, is unusual in two ways: (i) each of the 3 terms are prime,
and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the 3 terms in this
sequence?
*/
