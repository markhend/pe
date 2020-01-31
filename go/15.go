package main

import "fmt"

func main() {
	r, n := 1.0, 20.0
	for i := float64(1); i < n+1; i++ {
		r *= n/i + 1
		fmt.Println("n, i, r:", n, i, int64(r))
	}
	fmt.Println(int64(r))
}
