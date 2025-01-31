package utils

import (
	"image"
	"log"
	"net/http"
)

func GetDecodedJPEG(url string) image.Image {
	response, err := http.Get(url)
	if err != nil {
		log.Printf("Erro ao baixar a imagem: %s\n", err)
		panic(err)
	}

	defer response.Body.Close()

	img, _, err := image.Decode(response.Body)
	if err != nil {
		log.Printf("Erro ao decodificar a imagem: %s\n", err)
		panic(err)
	}

	return img
}