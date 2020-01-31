#include <stdio.h>

int main(void) {

    long mem[1000];
    int i;
    for (i = 0; i < 1000; i++) mem[i] = 0;

int P(int n) {
    int k, a, b, c, sum;
    if (n < 0) return 0;
    else if (n < 2) return 1;
    else if (mem[n]) return mem[n];
    else {
        sum = 0;
        for (k = 1; k <= n; k++) {
            a = n-k*(3*k-1)/2;
            b = n-k*(3*k+1)/2;
            if (k % 2) c = 1;
            else c = -1;
            sum += c * (P(a) + P(b));
        }
        mem[n] = sum;
        return sum;
    }
}
    //for (i = 1; i < 101; i++) printf("P(%d) is %d\n", i, P(i));
    printf("answer is %d\n", P(100) - 1);
    return 0;
}

/*
P(n) = SUM k=1->n (-1)^k+1 [P(n-1/2*k(3k-1)) + P(n-1/2*k(3k+1)]
It is possible to write five as a sum in exactly six different ways, seven ways
if you count five itself.
     4 + 1
     3 + 2
     3 + 1 + 1
     2 + 2 + 1
     2 + 1 + 1 + 1
     1 + 1 + 1 + 1 + 1
How many different ways can one hundred be written as a sum of at least two
positive integers?
By convention, P(0) = 1 and P(n) = 0 for negative n.
The first ten partition numbers are 1, 2, 3, 5, 7, 11, 15, 22, 30, and 42.
*/
