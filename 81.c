#include <stdio.h>

#define ROWS 80 
#define COLS 80

int main(void) {
    int i, j, a[ROWS][COLS];
    FILE *fp = fopen("matrix.txt", "r");
    for (i = 0; i < ROWS; i++)
        for (j = 0; j < COLS; j++) {
            fscanf(fp, "%d,", &a[i][j]);
            // printf("%d ", a[i][j]);
        }
    fclose(fp);
    
    for (i = ROWS - 1; i >= 0; i--) {
        for (j = COLS - 1; j >= 0; j--) {
            if (i == ROWS - 1 && j == COLS - 1) continue;
            else if (i == ROWS - 1) a[i][j] += a[i][j+1];
            else if (j == COLS - 1) a[i][j] += a[i+1][j];
            else a[i][j] += (a[i+1][j] < a[i][j+1] ? a[i+1][j] : a[i][j+1]);
        }
    }
    printf("answer is %d\n", a[0][0]);
    return 0;
}

/*
In the 5 by 5 matrix below, the minimal path sum from the top left to the
bottom right, by only moving to the right and down, is indicated in bold red
and is equal to 2427.


131 673 234 103 18
201 96  342 965 150
630 803 746 422 111
537 699 497 121 956
805 732 524 37  331

Find the minimal path sum in matrix.txt, a 31K text file containing an 80 by
80 matrix, from the top left to the bottom right by only moving right and down.
*/
