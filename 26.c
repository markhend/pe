#include <stdio.h>

int main(int argc, char *argv[]) {
	
    double n=0;
    int i;

    for (i = 2; i < 20; i++) {
    	printf("%.20Lf\n", 1.0/i);
    }

    return 0;
}
