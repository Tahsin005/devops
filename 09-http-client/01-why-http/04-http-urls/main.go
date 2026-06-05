/*
HTTP URLs
A URL, or Uniform Resource Locator, is the address of another computer, or "server" on the internet. Part of the URL specifies where to reach the server, and part of it tells the server what information we want.



Put simply, a URL represents a piece of information on some computer somewhere. We can get access to it by making a request, and reading the response that the server replies with.

Assignment
I've updated the getIssueData() function to be a bit more flexible. It now takes a URL as a parameter.

Try running the code in its current state. You should notice an error because the URL we're using is invalid.
Fix the code so that the call to getIssueData function uses the provided issueURL.
This time the printed data won't be as ugly, I added a prettify function that adds some formatting.
*/

package main

import (
	"fmt"
	"log"
)

const issueURL = "https://api.boot.dev/v1/courses_rest_api/learn-http/issues"

func main() {
	issues, err := getIssueData(issueURL)
	if err != nil {
		log.Fatalf("error getting issue data: %v", err)
	}
	prettyData, err := prettify(string(issues))
	if err != nil {
		log.Fatalf("error prettifying data: %v", err)
	}
	fmt.Println(prettyData)
}
