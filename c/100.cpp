#include <stdio.h>
#include <float.h>
// #include <gmp.h>

int main()
{
	int done = 0;
	// long double  a, b, x=7071060000, y=10000000000;
	double  a = 707107000000, b = 1000000000000, c, d, chance;

	while (!done){
		c = a - 1;
		d = b - 1;
		chance = a/b * c/d;
		// printf("a %.0f  b %.0f  chance is %.19f\n", a, b, chance);
		if (chance == .5) done = 1;
		else if (a*c > .5*b*d) b++;
		else a++;
	}
	printf("a %.0f  b %.0f  chance is %.19f\n", a, b, chance);
	return 0;
}
