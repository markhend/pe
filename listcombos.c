#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define FALSE 0;
#define TRUE 1;

int main() {

    int m, n = 8, i, j, k; // mh added
    // srand(time(NULL)); // mh added
    // m = (rand() % n) + 1; // m will vary from 1 to n
    m = 9; n = 40;

    int a[40];
    for (i = 0; i < n; i++) a[i] = i + 1;

    // we want to print all possible C(n,m) combinations of selecting m objects out of n
    printf("Printing C(%d,%d) possible combinations ...\n", n, m);

    int p[10];
    // This is an adhoc algo that keeps m pointers to the next valid combination
    for (i = 0; i < m; i++) p[i] = i; // The p[.] contain indices to the a vector\
                                         whose elements constitute next combination
    int done = FALSE;
    while (!done) {
        // for (i = 0; i < m; i++) printf("%2d ", a[p[i]]);
        // printf("\n");
        
        // Update combination method:
        // Start with p[m-1]. Try to increment it.
        // If it is already at the end, then try moving p[m-2] ahead.
        // If this is possible, then reset p[m-1] to 1 more than (the new) p[m-2].
        // If p[m-2] can not also be moved, then try p[m-3].
        // Move that ahead. Then reset p[m-2] and p[m-1].
        // Repeat all the way down to p[0].
        // If p[0] can not also be moved, then we have generated all combinations.
        
        j = m - 1;
        i = 1;
        int move_found = FALSE;
        while ((j >= 0) && !move_found) {
            if (p[j] < (n - i)) {
                move_found = TRUE;
                p[j]++; // point p[j] to next index
                for (k = j + 1; k < m; k++)
                    p[k] = p[j] + (k - j);
            }
            else {
                j--;
                i++;
            }
        }
        if (!move_found) done = TRUE;
    }
}
