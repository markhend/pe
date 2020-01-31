#include <stdio.h>


int main(int argc, char **argv) {

    int i, n, s, tmp, count = 0;
    for (i = 1; i < 10000000; i++) {
        n = i;
        // printf("%d ", n);
        do {
            s = 0;
            tmp = 0;
            while (n) {
                tmp = n % 10;
                s += (tmp * tmp);
                n /= 10;
            }
            // printf("%d ", s);
            n = s;
        } while (s != 1 && s != 89);
        if (s == 89) count++;
        // printf("\n");
    }
    printf("count is %d\n", count);
    return 0;
}
            

/*
a number chain is created by continuously adding the square of the digits in a
number to form a new number until it has been seen before.

for example,

44 -> 32 -> 13 -> 10 -> 1 -> 1
85 -> 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89

therefore any chain that arrives at 1 or 89 will become stuck in an endless
loop. what is most amazing is that every starting number will eventually arrive
at 1 or 89.

how many starting numbers below ten million will arrive at 89?
*/
