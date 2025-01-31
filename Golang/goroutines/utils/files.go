package utils

import (
	"image"
	"image/jpeg"
	"log"
	"os"
)

func SaveJPEGFile(fileName string, img image.Image) {
	file, err := os.Create(fileName)
	if err != nil {
		log.Printf("Erro ao criar o arquivo: %s\n", err)
		return
	}

	defer file.Close()

	err = jpeg.Encode(file, img, nil)
	if err != nil {
		log.Printf("Erro ao salvar a imagem: %s\n", err)
		return
	}
}
