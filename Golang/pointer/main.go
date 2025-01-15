package main

import "fmt"

type Person struct {
	name string
  age int8
}

func main() {
	valor := Person{
    name: "Oscar", // Cada campo é armazenado em um endereço de memória
    age: 25,
  }

  // Referência da memória
  fmt.Println("Valor name em mem: ", &valor.name) 
  fmt.Println("Valor age em mem: ", &valor.age)

	test(&valor)
  test2(valor)

  fmt.Println("==============================")
  fmt.Println("Valor [name] em mem: ", valor.name) 
}

func test(valor *Person) {
  fmt.Println("==============================")

  // Referência da memória
	fmt.Println("Valor name em mem: ", &valor.name)
  fmt.Println("Valor age em mem: ", &valor.age)

  // Pega o valor do ponteiro
  fmt.Println("Valor name em mem: ", valor.name) 
  fmt.Println("Valor age em mem: ", valor.age)

  // Altera a referência
  valor.name = "TESTE"
}

// Cria uma cópia do valor passado por parâmetro
func test2(valor Person) {
  fmt.Println("==============================")
  
  // Não altera a referência
  valor.name = "TESTE 2"

	fmt.Println("Valor name em mem: ", &valor.name)
  fmt.Println("Valor age em mem: ", &valor.age)

  fmt.Println("Valor name em mem: ", valor.name) 
  fmt.Println("Valor age em mem: ", valor.age)
}
