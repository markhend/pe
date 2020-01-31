#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

#define ITERS 1000 

int digits(double number) {
    int digs = 0;
    double step = 1;
    while (step <= number) {
        digs++;
        step *= 10;
    }
    return digs ? digs : 1;
}

int main(void) {

    int i = 0, j = 0, count = 0;
    int num_digits, den_digits;
    //long long temp, num, den;
    double temp, num, den;

    for (i = ITERS; i > 0; i--) {

        num = 1;
        den = 2; 

        for (j = 0; j < i - 1; j++) {
            num += 2 * den;
            temp = num;
            num = den;
            den = temp;
            while (num > 100000) {
                num /= 10;
                den /= 10;
            }
        }
        num += den;

        num_digits = digits(num);
        den_digits = digits(den);
        if (num_digits > den_digits) {
        	count++;
            printf("%0.f/%0.f\n", num, den);
        }
    }
    printf("count is %d\n", count);
    
    return 0;
}
/*
It is possible to show that the square root of two can be expressed as an
infinite continued fraction.

 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5 1 + 1/(2 + 1/2) = 7/5 = 1.4 1 + 1/(2 + 1/(2 + 1/2)) = 17/12
= 1.41666...  1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth
expansion, 1393/985, is the first example where the number of digits in the
numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator
with more digits than denominator?
*/
