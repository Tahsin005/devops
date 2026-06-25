/*
JSON Syntax
JSON (JavaScript Object Notation), is a standard for representing structured data based on JavaScript's object syntax. It is commonly used to transmit data in web apps via HTTP. For example, The HTTP requests we have been making in this course have been returning Jello issues as JSON.

JSON supports the following primitive data types:

Strings, e.g. "Hello, World!"
Numbers, e.g. 42 or 3.14
Booleans, e.g. true
Null, e.g. null
And the following collection types:

Arrays, e.g. [1, 2, 3]
Object literals, e.g. {"key": "value"}
JSON is similar to JavaScript objects and Python dictionaries. Keys are always strings, and the values can be any data type, including other objects.

The following is valid JSON data:

{
    "movies": [
        {
            "id": 1,
            "title": "Iron Man",
            "director": "Jon Favreau",
            "favorite": true
        },
        {
            "id": 2,
            "title": "The Avengers",
            "director": "Joss Whedon",
            "favorite": false
        }
    ]
}

Assignment
Complete the issueList and userObject string constant values.

issueList is a JSON array containing two issues (object literals). It should have the following issues:
First issue object:
  id: 0 (number)
  name: "Fix the thing" (string)
  estimate: 0.5 (number)
  completed: false (boolean)

Second issue object:
  id: 1 (number)
  name: "Unstick the widget" (string)
  estimate: 30 (number)
  completed: false (boolean)

userObject is a JSON object literal that represents a Jello user. It should have the following fields:
name: "Wayne Lagner" (string)
role: "Developer" (string)
remote: true (boolean)

The tests check that your constants contain valid JSON with the expected shape and values.

You can use a backtick (`) to create a multi-line string in Go. This will make it easier to write the JSON data.
*/

package main

const issueList = `
[
	{
		"id": 0,
		"name": "Fix the thing",
		"estimate": 0.5,
		"completed": false
	},
	{
		"id": 1,
		"name": "Unstick the widget",
		"estimate": 30,
		"completed": false
	}
]
`

const userObject = `
{
	"name": "Wayne Lagner",
	"role": "Developer",
	"remote": true
}
`
