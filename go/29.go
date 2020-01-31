package main

import (
	"fmt"
	"math"
)

func main() {
	h := make(map[int]int)
	a := new(math.big.Int)
	b := new(math.big.Int)
	for i := 0; i < 100; i++ {
		for j := 0; j < 100; j++ {
			t = i + j
			h[t] = t
		}
	}
	fmt.Println("h has len", len(h))
}
