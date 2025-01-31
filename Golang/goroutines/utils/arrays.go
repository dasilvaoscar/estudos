package utils

func CustomArrayString(data string, length int) []string {
	re := []string{}
	for i := 0; i != length; i++ {
		re = append(re, data)
	}

	return re
}