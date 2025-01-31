package main

import (
	"goroutine-test/utils"
	"log"
	"os"
	"sync"
	"time"

	"github.com/google/uuid"
)

const GO_ROUTINE_IMAGE_FOLDER = "tests-goroutine"
const SEQUENTIAL_IMAGE_FOLDER = "tests-sequential"

func saveImageRoutine(url string, wg *sync.WaitGroup, fileChan chan string) {
	defer wg.Done()

	img := utils.GetDecodedJPEG(url)
	fileName := GO_ROUTINE_IMAGE_FOLDER + "/imagem_baixada" + uuid.NewString() + ".jpg"
	utils.SaveJPEGFile(fileName, img)

	fileChan <- fileName
}

func saveImageConcurrent(urls []string) {
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
		go saveImageRoutine(url, &wg, fileChan)
	}

	wg.Wait()
	close(fileChan)

	elapsed := time.Since(start)
	log.Printf("Goroutine time: %s\n", elapsed)
}

func saveImageSequential(urls []string) {
	dirName := "tests-default"

	if err := os.Mkdir(dirName, 0755); err != nil {
		os.RemoveAll(dirName)
		os.Mkdir(dirName, 0755)
	}

	start := time.Now()

	for _, url := range urls {
		img := utils.GetDecodedJPEG(url)
		fileName := dirName + "/imagem_baixada" + uuid.NewString() + ".jpg"
		utils.SaveJPEGFile(fileName, img)
	}

	elapsed := time.Since(start)
	log.Printf("Sequential time: %s\n", elapsed)
}

func main() {
	link := "https://images.wallpapersden.com/image/download/radagon-4k-elden-ring_bWhnZ2eUmZqaraWkpJRobWllrWdma2U.jpg"

	images := utils.CustomArrayString(link, 10)

	saveImageConcurrent(images)
	saveImageSequential(images)
}
