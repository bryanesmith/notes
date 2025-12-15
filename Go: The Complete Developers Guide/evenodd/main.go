// You can edit this code!
// Click here and start typing.
package main

import "fmt"

func main() {
	vals := []int{}
	for i := 0; i <= 10; i++ {
		vals = append(vals, i)
	}
	for _, v := range vals {
		var msg string
		if v%2 == 0 {
			msg = "even"
		} else {
			msg = "odd"
		}
		fmt.Println(v, "is", msg)
	}
}
