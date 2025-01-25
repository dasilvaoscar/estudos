package main

import (
	"encoding/json"
	"log"
)

type User struct {
	Name  string `json:"test1"`
	Email string `json:test2`
}

func main() {
	jsonData, _ := json.Marshal(User{Name: "Oscar", Email: "oscar.silva@gmail.com"})
	log.Println("User JSON:", string(jsonData))

	var userEntity User
	if err := json.Unmarshal(jsonData, &userEntity); err == nil {
		log.Println("Entity again:", userEntity)
	}
}
