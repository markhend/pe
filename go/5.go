package main

import (
	"euler"
	"fmt"
	//"strconv"
)

func main() {
	x := 6 // lcm(2, 3)
	for i := 4; i < 21; i++ {
		x = euler.Lcm(x, i)
		// fmt.Println(i, x)
	}
	fmt.Println(x)
}
