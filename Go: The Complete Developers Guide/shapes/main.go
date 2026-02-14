package main

import "fmt"

type shape interface {
	getArea() float64
}

type triange struct {
	base   float64
	height float64
}

func (t triange) getArea() float64 {
	return 0.5 * t.base * t.height
}

type square struct {
	side float64
}

func (s square) getArea() float64 {
	return s.side * s.side
}

func printArea(s shape) {
	fmt.Printf("area is %f\n", s.getArea())
}

func main() {
	t := triange{base: 10, height: 5}
	printArea(t)

	s := square{side: 4}
	printArea(s)
}
