package main

import (
	"euler"
	"fmt"
)

func main() {
	r := int64(0)
	for _, v := range euler.Primes(2000000) {
		r += v
	}
	fmt.Println(r)
}
