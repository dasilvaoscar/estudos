package main

import "fmt"

func main() {
	const int8Unsigned uint8 = 255                    // 0 até 255
	const int16Unsigned uint16 = 65535                // 0 até 65.535
	const int32Unsigned uint32 = 4294967295           // 0 até 4.294.967.295
	const int64Unsigned uint64 = 18446744073709551615 // 0 até 18.446.744.073.709.551.615

	fmt.Println("uint8:", int8Unsigned)
	fmt.Println("uint16:", int16Unsigned)
	fmt.Println("uint32:", int32Unsigned)
	fmt.Println("uint64:", int64Unsigned)

	// Números com sinal (signed)
	const int8Signed int8 = -128                   // -128 até 127
	const int16Signed int16 = -32768               // -32.768 até 32.767
	const int32Signed int32 = -2147483648          // -2.147.483.648 até 2.147.483.647
	const int64Signed int64 = -9223372036854775808 // -9.223.372.036.854.775.808 até 9.223.372.036.854.775.807

	fmt.Println("int8:", int8Signed)
	fmt.Println("int16:", int16Signed)
	fmt.Println("int32:", int32Signed)
	fmt.Println("int64:", int64Signed)
}
