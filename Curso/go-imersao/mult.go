package main

import (
	"fmt"
	"time"
)

func worker(workerID int, data chan int) {
	for x := range data {
		fmt.Printf("Worker %d received %d\n", workerID, x)
		time.Sleep(time.Second)
	}
}

// T1
func main() {
	channel := make(chan int)
	// go worker(1, channel) // T2
	// go worker(2, channel) // T2
	// go worker(3, channel) // T2

	for i := 0; i < 1000000; i++ {
		go worker(i, channel) // T2
	}
	for i := 0; i < 1000000; i++ {
		channel <- i
	}
}
