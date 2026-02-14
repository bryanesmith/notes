package main

import "fmt"

type shape interface {
	printArea()
	getArea() float64
}

type triange struct {
	base   float64
	height float64
}

func (t triange) getArea() float64 {
	return 0.5 * t.base * t.height
}

func (t triange) printArea() {
	fmt.Printf("area of triangle is %f\n", t.getArea())
}

type square struct {
	side float64
}

func (s square) getArea() float64 {
	return s.side * s.side
}

func (s square) printArea() {
	fmt.Printf("area of square is %f\n", s.getArea())
}

func main() {
	t := triange{base: 10, height: 5}
	s := square{side: 4}

	t.printArea()
	s.printArea()
}
