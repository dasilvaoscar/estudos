package main

import (
	"errors"
	"fmt"
	"math/rand"
	"time"
)

func randomNuber() int {
	rand.Seed(time.Now().UnixNano())
	randomNum := rand.Intn(100)
	return randomNum
}

func FullName(first_name, last_name string) (string, error) {
	if randomNuber() % 2 != 0 {
		return "", errors.New("random error")
	}

	full_name := fmt.Sprintf("%s %s", first_name, last_name)
	return full_name, nil
}

func main() {
	full_name, is_error := FullName("Oscar", "da Silva")

	if is_error == nil {
		fmt.Println(full_name)
	}
}


