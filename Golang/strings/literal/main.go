package main

import "fmt"

func main() {
	string1 := "Lerem \nIpsum"
	string2 := `Lorem \nIpsum`
	string3 := `Lorem 
	Ipsum`

	fmt.Println("String literal:", string1)
	fmt.Println("---------------------------------")
	fmt.Println("Row string literal:", string2)
	fmt.Println("---------------------------------")
	fmt.Println("Row string literal:", string3)
}
