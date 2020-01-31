package main

import (
	"fmt"
	"math"
)

func main() {
	lo := math.Sqrt(1020304050607080900)
	hi := math.Sqrt(1929394959697989990)
	fmt.Println(lo, hi)
}

/* Find the unique positive integer whose square has the form:

    1_2_3_4_5_6_7_8_9_0

where each "_" is a single digit */
