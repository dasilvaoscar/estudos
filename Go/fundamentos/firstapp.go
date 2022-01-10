package main

import "fmt"

// import "fmt"

func main() {
	msg := func() string {
		return "Hello World " + returnStringName("Oscar")
	}
	fmt.Println(msg())
}

func returnStringName(name string) string {
	return name
}
