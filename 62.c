#include <stdio.h>

int a[20];

void sortArr(int a[], int n) {
    int i, j, tmp;
    for (i = 0; i < n - 1; i++)
        for (j = i + 1; j < n; j++)
            if (a[j] > a[i]) {
                tmp = a[i];
                a[i] = a[j];
                a[j] = tmp;
            }
}

void intToArr(long long n, int len) {
    int i;
    for (i = len - 1; i >= 0; i--) {
        a[i] = n % 10;
        n -= a[i];
        n /= 10;
    }
    a[i] = n;
}

long long arrToInt(int a[], int len) {
    int i;
    long long n = 0;
    for (i = 0; i < len - 1; i++) {
        n += a[i];
        n *= 10;
    }
    n += a[i];
    return n;
}

long long perm(long long n) {
    int digits = 0;
    long long tmp = n;
    do {
        n /= 10;
        digits++;
    } while (n > 0);
    intToArr(tmp, digits);
    int i;
    sortArr(a, digits);
    return (arrToInt(a, digits));
}

int main(void) {

    long long i;
    int cnt;
    long long cubes[100000];
    for (i = 0; i < 100000; i++) cubes[i] = 0;
    for (i = 300; i < 100000; i++) {
        cubes[i] = perm(i*i*i);
        int j;
        cnt = 1;
        for (j = 0; j < i; j++) 
            if (cubes[j] == cubes[i]) cnt++;
        if (cnt == 5) break;
    }
    int tmp = i;
    for (i = 0; i < 100000; i++)
        if (cubes[i] == cubes[tmp]) printf("answer is %d^3\n", i);
    return 0;
}    

/*The cube, 41063625 (345^3), can be permuted to produce two other cubes:
56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube
which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are
cube.
*/
