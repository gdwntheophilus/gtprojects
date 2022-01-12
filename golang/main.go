package main

import (
	"fmt"

	"rsc.io/quote"
)

func connectDbInstance(url string, username string, password string) string {
	connectionString := fmt.Sprintf("%v:%v:%v", url, username, password)
	return connectionString
}

func main() {
	fmt.Println("Server is booting")
	fmt.Println(quote.Go())
	fmt.Println(connectDbInstance("url", "username", "password"))
}
