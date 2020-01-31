package main

import (
	"fmt"
)

func main() {
	ans, max := 1, 0
	for i := 1; i < 1000000; i++ {
		n, cnt := int64(i), 0
		for n > 1 {
			cnt++
			if n%2 == 0 {
				n /= 2
			} else {
				n = 3*n + 1
			}
		}
		if cnt > max {
			ans, max = i, cnt
		}
	}
	fmt.Println(ans, max)
}
