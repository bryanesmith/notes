package main

import (
	"os"
	"testing"
)

func TestNewDeck(t *testing.T) {
	d := newDeck()

	if len(d) != 52 {
		t.Errorf("Expected deck length of 52, but got %v", len(d))
	}

	aceOfSpadesFound, kingOfClubsFound := 0, 0

	for _, card := range d {
		if card == "Ace of Spades" {
			aceOfSpadesFound++
		}
		if card == "King of Clubs" {
			kingOfClubsFound++
		}
	}

	if aceOfSpadesFound != 1 {
		t.Errorf("Expected to find one Ace of Spades, but found %v", aceOfSpadesFound)
	}

	if kingOfClubsFound != 1 {
		t.Errorf("Expected to find one King of Clubs, but found %v", kingOfClubsFound)
	}
}

func TestSaveToDeckAndNewDeckFromFile(t *testing.T) {
	filename := "deck_test.txt"

	// In case previous test failed
	os.Remove(filename)

	d := newDeck()
	d.saveToFile(filename)
	loadedDeck, err := newDeckFromFile(filename)
	if err != nil {
		t.Errorf("Error loading deck from file: %v", err)
	}

	if len(loadedDeck) != len(d) {
		t.Errorf("Expected deck length of %v, but got %v", len(d), len(loadedDeck))
	}

	os.Remove(filename)
}
