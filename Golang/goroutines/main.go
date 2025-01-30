package main

import (
	"image"
	"image/jpeg"
	"log"
	"net/http"
	"os"
	"sync"
	"time"

	"github.com/google/uuid"
)

func getImageConcurrent(urls []string) []string {
	dirName := "tests-goroutine"

	if err := os.Mkdir(dirName, 0755); err != nil {
		os.RemoveAll(dirName)
		os.Mkdir(dirName, 0755)
	}

	var wg sync.WaitGroup
	fileChan := make(chan string, len(urls))

	start := time.Now()

	for _, url := range urls {
		wg.Add(1)
		go func(url string) {
			defer wg.Done()

			response, err := http.Get(url)
			if err != nil {
				log.Printf("Erro ao baixar a imagem: %s\n", err)
				return
			}
			defer response.Body.Close()

			img, _, err := image.Decode(response.Body)
			if err != nil {
				log.Printf("Erro ao decodificar a imagem: %s\n", err)
				return
			}

			fileName := dirName + "/imagem_baixada" + uuid.NewString() + ".jpg"

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

			fileChan <- fileName
		}(url)
	}

	wg.Wait()
	close(fileChan)

	allFiles := []string{}
	for fileName := range fileChan {
		allFiles = append(allFiles, fileName)
	}

	elapsed := time.Since(start)
	log.Printf("Goroutine %s\n", elapsed)

	return allFiles
}

func getImageSequential(urls []string) []string {
	dirName := "tests-default"

	if err := os.Mkdir(dirName, 0755); err != nil {
		os.RemoveAll(dirName)
		os.Mkdir(dirName, 0755)
	}

	allFiles := []string{}

	start := time.Now()

	for _, url := range urls {
		response, err := http.Get(url)
		if err != nil {
			log.Printf("Erro ao baixar a imagem: %s\n", err)
			continue
		}

		defer response.Body.Close()

		img, _, err := image.Decode(response.Body)
		if err != nil {
			log.Printf("Erro ao decodificar a imagem: %s\n", err)
			continue
		}

		fileName := dirName + "/imagem_baixada" + uuid.NewString() + ".jpg"

		file, err := os.Create(fileName)
		if err != nil {
			log.Printf("Erro ao criar o arquivo: %s\n", err)
			continue
		}

		defer file.Close()

		err = jpeg.Encode(file, img, nil)
		if err != nil {
			log.Printf("Erro ao salvar a imagem: %s\n", err)
			continue
		}

		allFiles = append(allFiles, fileName)
	}

	elapsed := time.Since(start)
	log.Printf("Sequential %s\n", elapsed)

	return allFiles
}

func customArrayString(data string, length int) []string {
	re := []string{}
	for i := 0; i != length; i++ {
		re = append(re, data)
	}

	return re
}

func main() {
	link := "https://images.wallpapersden.com/image/download/radagon-4k-elden-ring_bWhnZ2eUmZqaraWkpJRobWllrWdma2U.jpg"

	images := customArrayString(link, 50)

	// Execução concorrente
	getImageConcurrent(images)
	
	// Execução sequencial
	getImageSequential(images)
}