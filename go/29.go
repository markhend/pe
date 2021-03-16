package main

import (
	"fmt"
	"math/big"
)

func main() {
	h := make(map[int]int)
	a := new(big.Int)
	b := new(big.Int)
	// Next 2 lines added to let compile
	a = b
	fmt.Println(a)
	for i := 0; i < 100; i++ {
		for j := 0; j < 100; j++ {
			t := i + j
			h[t] = t
		}
	}
	fmt.Println("h has len", len(h))
}
