package main

import (
	"fmt"
	"os"
)

func main() {
	cards := newDeck()
	cards.shuffle()
	hand, cards := cards.deal(5)
	hand.print()

	filename := "my_cards.txt"
	cards.saveToFile(filename)
	newDeck, err := newDeckFromFile(filename)
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	newDeck.print()
}
