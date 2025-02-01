package main

import (
	"log"
)

func main() {
	const float_32 float32 = 3.4028235e+38           // -3.4028235e+38 até 3.4028235e+38
	const float_64 float64 = 1.7976931348623157e+308 // -2.2250738585072014e-308 até 1.7976931348623157e+308

	log.Println("\n\n-----------Float-----------")
	log.Println("int32Unsigned:", float_32)
	log.Println("int64Unsigned:", float_64)
}
