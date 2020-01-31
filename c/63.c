#include <stdio.h>
#include <math.h>

int main() {

    int i, count = 9; // 1-9 are all 1st powers
    for (i = 2; i < 100; i++) {
        printf("i is %d\n", i);
        double b = 2;
        // printf("b is %f\n", b);
        while (pow(b, i) < pow(10.0, i)) {
            if (pow(b, i) >= pow(10.0, i-1) && pow(b, i) < pow(10.0, i)) 
                count++;
            b++;
            // printf("b is %f\n", b);
        }
    }
    printf("count is %d\n", count);
    return 0;
}


// The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit
// number, 134217728=8^9, is a ninth power.
//
// How many n-digit positive integers exist which are also an nth power?
