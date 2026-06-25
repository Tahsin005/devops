/*
Unmarshal JSON
We can decode JSON bytes (or strings) into a Go struct using json.Unmarshal or a json.Decoder.

The Decode method of json.Decoder streams data from an io.Reader into a Go struct, while json.Unmarshal works with data that's already in []byte format. Using a json.Decoder can be more memory-efficient because it doesn't load all the data into memory at once. json.Unmarshal is ideal for small JSON data you already have in memory. When dealing with HTTP requests and responses, you will likely use json.Decoder since it works directly with an io.Reader.

Example
// res is an http.Response
defer res.Body.Close()

data, err := io.ReadAll(res.Body)
if err != nil {
	return nil, err
}

var issues []Issue
if err := json.Unmarshal(data, &issues); err != nil {
    return nil, err
}

Assignment
Update the getIssueData function in http.go.

Change the return signature to return []Issue instead of []byte.
Because the function will now return a decoded slice of issues, change the name from getIssueData to getIssues.
Get the data from the response body using io.ReadAll, creating a slice of bytes []byte.
Create a nil slice of issues []Issue.
Use json.Unmarshal on the data to get the JSON data.
Return the issues.
*/

package main

import (
	"encoding/json"
	"fmt"
	"io"
	"net/http"
)

func getIssues(url string) ([]Issue, error) {
	res, err := http.Get(url)
	if err != nil {
		return nil, fmt.Errorf("error creating request: %w", err)
	}
	defer res.Body.Close()

	var issues []Issue
	data, err := io.ReadAll(res.Body)
	if err != nil {
		return nil, err
	}

	err = json.Unmarshal(data, &issues)
	if err != nil {
		return nil, err
	}

	return issues, nil
}