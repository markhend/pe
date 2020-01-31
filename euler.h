#include <math.h>

int isprime(long n) {
    if (n % 2 == 0) return 0;
    if (n < 2) return 0;
    long x;
    for (x = 2; x*x <= n; x++)
        if (n % x == 0) return 0;
    return 1;
}

int gcd(int a, int b) {
    int tmp;
    while (b) {
        tmp = a;
        a = b;
        b = tmp % b;
    }
    return a;
}

int lcm(int a, int b) {
    int tmp, ab = a * b;
    while (b) {
        tmp = a;
        a = b;
        b = tmp % b;
    }
    return ab / a;
}

void swap(int *a, int *b) {
    int tmp;
    tmp = *a;
    *a = *b;
    *b = tmp;
}

int nextPerm(int arr[], int n) {
    int i = n - 1, tmp;
    while (arr[i-1] >= arr[i] && i > 0)
        i--;
    if (i == 0) return -1;
    int j = n;
    while (arr[j-1] <= arr[i-1] && j > 0)
        j--;
    tmp = arr[i-1];
    arr[i-1] = arr[j-1];
    arr[j-1] = tmp;
    i++; j = n;
    while(i < j) {
        tmp = arr[i-1];
        arr[i-1] = arr[j-1];
        arr[j-1] = tmp;
        i++;
        j--;
    }
}

void primes(int arr[], int upto) {

    int i, j;

    for (i = 2; i < upto; i++) arr[i] = 1;
    i = 2;
    j = i + i;
    while (i < sqrt((double)upto)) {
        while (j < upto) {
            arr[j] = 0;
            j += i;
        }
        i++;
        while (arr[i] == 0) i++;
        j = i + i;
    }
}
