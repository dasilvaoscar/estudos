package main

import "fmt"

func main() {
	array_1 := [2]int8{1, 2} // cap 2
	slice_1 := []int8{1, 2} // cap 2

	slice_1 = append(slice_1, 2, 3) // cap = 8 | 2x o len 

	fmt.Println("Array cap", cap(array_1))
	fmt.Println("Slice cap", cap(slice_1))

	slice_1 = make([]int8, 1023)
	slice_1 = append(slice_1, 1) // cap = 1536 | len + 25% 
	fmt.Println("Slice cap", cap(slice_1))
}