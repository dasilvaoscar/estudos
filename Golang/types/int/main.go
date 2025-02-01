package main

import (
	"log"
)

func main() {
	const int8Unsigned uint8 = 255                    // 0 até 255
	const int16Unsigned uint16 = 65535                // 0 até 65.535
	const int32Unsigned uint32 = 4294967295           // 0 até 4.294.967.295
	const int64Unsigned uint64 = 18446744073709551615 // 0 até 18.446.744.073.709.551.615

	const int8Signed int8 = -128                   // -128 até 127
	const int16Signed int16 = -32768               // -32.768 até 32.767
	const int32Signed int32 = -2147483648          // -2.147.483.648 até 2.147.483.647
	const int64Signed int64 = -9223372036854775808 // -9.223.372.036.854.775.808 até 9.223.372.036.854.775.807

	log.Println("\n\n-----------Unsigned Integers-----------")
	log.Println("int8Unsigned:", int8Unsigned)
	log.Println("int16Unsigned:", int16Unsigned)
	log.Println("int32Unsigned:", int32Unsigned)
	log.Println("int64Unsigned:", int64Unsigned)

	log.Println("\n\n-----------Signed Integers-----------")
	log.Println("int8Signed:", int8Signed)
	log.Println("int16Signed:", int16Signed)
	log.Println("int32Signed:", int32Signed)
	log.Println("int64Signed:", int64Signed)
}
