/*
Marshal JSON
If there is a way to unmarshal JSON data, there must be a way to marshal it as well. The json.Marshal function converts a Go struct into a slice of bytes representing JSON data.

Example
type Board struct {
	Id       int    `json:"id"`
	Name     string `json:"name"`
	TeamId   int    `json:"team"`
	TeamName string `json:"team_name"`
}

board := Board{
	Id:       1,
	Name:     "API",
	TeamId:   9001,
	TeamName: "Backend",
}

data, err := json.Marshal(board)
if err != nil {
	log.Fatal(err)
}
fmt.Println(string(data))
// {"id":1,"name":"API","team":9001,"team_name":"Backend"}


Assignment
Complete the marshalAll function. It accepts a slice of "items", which can be of any type. The expectation is that they are structs of various forms. It should return a slice of slices of bytes (I didn't stutter) [][]byte.

Create a slice of bytes slices to hold the marshalled data.
For each item in items:
Marshal the item into a slice of bytes.
If an item cannot be marshaled, immediately return a nil slice and the error.
Add the marshalled JSON byte slice to the slice of bytes slices.
Return the marshalled data in the same order as the input items.
*/
package main

import (
	"encoding/json"
)

func marshalAll[T any](items []T) ([][]byte, error) {
	var data [][]byte

	for _, item := range items {
		jsonOutput, err := json.Marshal(item)
		if err != nil {
			return nil, err
		}
		data = append(data, jsonOutput)
	}

	return data, nil
}
