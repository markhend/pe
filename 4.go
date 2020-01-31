package main

import (
	"euler"
	"fmt"
	"strconv"
)

func main() {
	max := 0
	for i := 100; i < 1000; i++ {
		for j := i + 1; j < 1000; j++ {
			if i*j > max && euler.IsPal(strconv.Itoa(i*j)) {
				max = i * j
			}
		}
	}
	fmt.Println(max)
	return
}
