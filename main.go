package main

import (
	"encoding/csv"
	"log"
	"math/rand"
	"os"
	"strconv"
	"time"
)

const (
	maxArraySize = 10000000
	step         = 100000
)

func sum(numbers []int) int {
	total := 0
	for i := range numbers {
		total += i
	}
	return total
}

func saveCSV(filename string, data []int64) {
	file, err := os.Create(filename)
	if err != nil {
		log.Fatalf("Error creating file: %v", err)
	}
	defer file.Close()

	writer := csv.NewWriter(file)
	defer writer.Flush()

	for _, value := range data {
		record := []string{strconv.FormatInt(value, 10)}
		err := writer.Write(record)
		if err != nil {
			log.Fatalf("Error writing to file: %v", err)
		}
	}
}

func main() {
	var numbers []int
	var result []int64

	for i := 0; i < maxArraySize; i++ {
		numbers = append(numbers, rand.Intn(maxArraySize))
	}

	for i := 0; i < len(numbers); i += step {
		testValues := numbers[0:i]
		start := time.Now()
		_ = sum(testValues)
		timeTaken := time.Since(start)
		result = append(result, timeTaken.Nanoseconds())
	}

	saveCSV("go_sum.csv", result)
}
