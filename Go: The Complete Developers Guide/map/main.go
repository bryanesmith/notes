package main

import "fmt"

func printMap(c map[string]string) {
	for color, hex := range c {
		fmt.Printf("%s => %s\n", color, hex)
	}
}

func main() {

	// var colors map[string]string

	// colors := make(map[string]string)

	// colors["white"] = "#FFFFFF"

	// delete(colors, "white")

	colors := map[string]string{
		"red":   "#FF0000",
		"green": "#4BF745",
		"white": "#FFFFFF",
	}

	printMap(colors)
}
