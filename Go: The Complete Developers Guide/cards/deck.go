package main

import (
	"fmt"
	"math/rand"
	"os"
	"strings"
	"time"
)

type deck []string

var Separator string = ","

func newDeck() deck {
	cards := deck{}

	suits := []string{"Spades", "Diamonds", "Hearts", "Clubs"}
	values := []string{"Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"}

	for _, suit := range suits {
		for _, value := range values {
			cards = append(cards, value+" of "+suit)
		}
	}

	return cards
}

func newDeckFromFile(filename string) (deck, error) {
	bs, err := os.ReadFile(filename)
	if err != nil {
		return nil, err
	}
	ss := string(bs)
	return strings.Split(ss, Separator), nil
}

func (d deck) print() {
	fmt.Println(d.toString())
}

func (d deck) deal(size int) (deck, deck) {
	if len(d) < size {
		return d, []string{}
	}
	return d[:size], d[size:]
}

func (d deck) toString() string {
	return strings.Join(d, Separator)
}

func (d deck) saveToFile(filename string) error {
	b := []byte(d.toString())
	return os.WriteFile(filename, b, 0666)
}

func (d deck) shuffle() {
	src := rand.NewSource(time.Now().UnixNano())
	r := rand.New(src)
	for i := range d {
		j := r.Intn(len(d) - 1)
		d[i], d[j] = d[j], d[i]
	}
}
