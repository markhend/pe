package main

import "fmt"

func main() {
	for a := 0; a < 1001; a++ {
		for b := a + 1; b < 1001; b++ {
			for c := b + 1; c < 1001; c++ {
				if a+b+c != 1000 {
					continue
				} else if a*a+b*b != c*c {
					continue
				} else {
					fmt.Println(a, b, c, a*b*c)
				}
			}
		}
	}
}
