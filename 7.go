package main

import (
	"euler"
	"fmt"
)

func main() {
	p := euler.Primes(1000000)
	fmt.Println(p[10000])
}
