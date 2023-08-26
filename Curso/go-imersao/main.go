// package main

// import (
// 	"encoding/json"
// 	"fmt"
// 	"net/http"
// 	"time"
// )

// func soma(x int, y int) (int, bool) {
// 	if x > 10 {
// 		return x + y, true
// 	}
// 	return x + y, false
// }

// type Course struct {
// 	Name        string  `json:"course"`
// 	Description string  `json:"description"`
// 	Price       float32 `json:"price"`
// }

// func (c Course) GetFullInfo() string {
// 	return fmt.Sprintf("Name: %s, Description %s, Price: %f", c.Name, c.Description, c.Price)
// }

// func home(w http.ResponseWriter, r *http.Request) {
// 	course := Course{
// 		Name:        "Golang",
// 		Description: "Imersão Golang",
// 		Price:       100,
// 	}
// 	course.Price = 0.5

// 	json.NewEncoder(w).Encode(course)

// 	// w.Write([]byte("Hello World"))
// }

// func counter() {
// 	for i := 0; i < 10; i++ {
// 		fmt.Println(i)
// 		time.Sleep(time.Second)
// 	}
// }

// func main() {
// 	// var a string
// 	// a = "Hello, World!"
// 	// println(a)
// 	// b := "Hello, World!"
// 	// print(b)
// 	// b = "Oi mundo"
// 	// print(b)

// 	// println(soma(1, 2))
// 	// resultado, soma := soma(10, 20)
// 	// print(resultado, " ", soma)

// http.HandleFunc("/", home)
// http.ListenAndServe(":8080", nil)

// 	println("Primeiro counter iniciado")
// 	go counter()
// 	println("Segundo counter iniciado")
// 	go counter()
// 	println("Terceiro counter iniciado")
// 	counter()

// }
