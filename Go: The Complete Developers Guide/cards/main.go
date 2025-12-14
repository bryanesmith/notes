package main

func main() {
	cards := newDeck()
	hand, cards := cards.deal(5)

	hand.print()
	cards.print()
}
