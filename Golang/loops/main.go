package main

import "fmt"

func forLoopOfStringArray(data []string) {
	for i, current := range data {
		fmt.Printf("Index: %d, Current value: %s\n", i, current)
	}
}

func forLoopOfMap(data map[string]string) {
	for key, value := range data {
		fmt.Printf("\nKey: %s, Value: %s", key, value)
	}
}

func forLoopOfMapArray(data []map[string]string) {

}

func main() {
	string_array := []string{"João", "André", "Mateus"}
	forLoopOfStringArray(string_array)

	string_object := map[string]string{"name": "Oscar", "email": "oscarkaka222@gmail.com"}
	forLoopOfMap(string_object)
}
