package main

import (
	//"euler"
	"fmt"
	//"strconv"
)

func main() {
	a, b := 0, 0
	for i := 1; i < 101; i++ {
		a += i * i
		b += i
	}
	fmt.Println(b*b - a)
}
