package main

import (
	"euler"
	"fmt"
)

/* Triangle numbers are sum of seq up to n, e.g.
T(3) = 1+2+3 = 6 and also (n(n+1))/2.
Num divisors of n (D) is the product of
the exponents of the distinct prime divisors, e.g.
28 = 2*2*7 so D(28) = (2+1) * (1+1) = 6
*/

func main() {
	n := 3
	facs := []int{}
	for t := 6; ; t += n {
		facs = euler.Factors(t)
		cnt, tot := 1, 1
		for i, v := range facs[1:] {
			if v == facs[i] {
				cnt++
			} else {
				tot *= (cnt + 1)
				cnt = 1
			}
		}
		tot *= (cnt + 1) // accounting for last el of facs
		// fmt.Println(t, facs, tot)
		if tot > 500 {
			fmt.Println(t, facs, tot)
			return
		}
		n++
	}
}
