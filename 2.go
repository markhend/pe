package main

import "fmt"

func main() {
	ans := 0
	prev, curr := 1, 2
	for curr < 4*1e6 {
		if curr%2 == 0 {
			ans += curr
		}
		prev, curr = curr, prev+curr
	}
	fmt.Println(ans)
}
