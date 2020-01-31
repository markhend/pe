package main

import (
	"fmt"
	"math"
)

func main() {
	//What is the largest prime factor of
	var n int64 = 600851475143
	sqrtN := int64(math.Sqrt(float64(n))) + 1
	for i := sqrtN; i > 1; i -= 2 {
		if n%i == 0 && isPrime(i) {
			fmt.Println(i)
			break
		}
	}
	return
}

func isPrime(n int64) bool {
	if n < 2 {
		return false
	} else if n < 4 {
		return true
	} else {
		for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
			if n%int64(i) == 0 {
				return false
			}
		}
	}
	return true
}
