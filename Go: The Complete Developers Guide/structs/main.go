package main

import (
	"fmt"
)

type person struct {
	firstName   string
	lastName    string
	contactInfo // same as "contactInfo contactInfo"
}

type contactInfo struct {
	email string
	zip   int
}

func (p person) print() {
	fmt.Printf("%+v\n", p)
}

func (p *person) updateName(newFirstName string) {
	// Equivalent to (*p).firstName = newFirstName
	p.firstName = newFirstName
}

func main() {
	var alex person
	alex.firstName = "Alex"
	alex.lastName = "Anderson"
	alex.contactInfo = contactInfo{email: "alex@example.org", zip: 12345}
	alex.print()

	jim := person{
		firstName: "Jim",
		lastName:  "Party",
		contactInfo: contactInfo{
			email: "jim@example.org",
			zip:   94000,
		},
	}

	// Equivalent to:
	// 	jimPtr := &jim
	//	jimPtr.updateName("Jimmy")
	jim.updateName("Jimmy")
	jim.print()
}
