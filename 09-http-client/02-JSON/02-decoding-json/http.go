/*
Decoding JSON
When we receive JSON data in the body of an HTTP response, it comes as a stream of bytes. As we saw before, we can just convert the bytes to a string... but in Go there's a better way. It's typically best to decode the JSON data into a struct.

Take this example JSON data:

[
  {
    "id": "001-a",
    "title": "Unspaghettify code",
    "estimate": 9001
  }
]

To decode this JSON into a slice of Issue structs, we need to know the JSON fields and their types. The standard encoding/json package uses tags to map JSON fields to struct fields.

Struct fields must be exported (capitalized) to decode JSON.

type Issue struct {
	Id       string `json:"id"`
	Title    string `json:"title"`
	Estimate int    `json:"estimate"`
}

After receiving the response, we can decode it into a slice of Issues with the "address of" operator &:

// res is a successful `http.Response`

var issues []Issue
decoder := json.NewDecoder(res.Body)
if err := decoder.Decode(&issues); err != nil {
    fmt.Println("error decoding response body")
    return
}

If no error occurs, we can use the slice of items in our program.

for _, issue := range issues {
    fmt.Printf("Issue – id: %v, title: %v, estimate: %v\n", issue.Id, issue.Title, issue.Estimate)
    // Issue – id: 001-a, title: Unspaghettify code, estimate: 9001
}

Assignment
In previous lessons, we've converted response into slices of bytes, and then strings. Now, decode the response data directly into a slice of issues and return that instead.

Import the json package from "encoding/json".
Create a nil slice of items []Issue.
Create a new *json.Decoder using json.NewDecoder.
Decode the response body using the decoder's Decode method.
Return the slice of issues.
If any error occurs return a nil slice and the error.
*/

package main

import (
	"fmt"
	"net/http"
	"encoding/json"
)

func getIssues(url string) ([]Issue, error) {
	res, err := http.Get(url)
	if err != nil {
		return nil, fmt.Errorf("error creating request: %w", err)
	}
	defer res.Body.Close()

	var issues []Issue
	decoder := json.NewDecoder(res.Body)
	if err := decoder.Decode(&issues); err != nil {
	    fmt.Println("error decoding response body")
	    return nil, err
	}
	return issues, nil
}
