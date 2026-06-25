package main

import (
	"encoding/json"
	"fmt"
	"testing"
)

type Issue struct {
	ID        *int     `json:"id"`
	Name      *string  `json:"name"`
	Estimate  *float64 `json:"estimate"`
	Completed *bool    `json:"completed"`
}

type User struct {
	Name   *string `json:"name"`
	Role   *string `json:"role"`
	Remote *bool   `json:"remote"`
}

var expectedIssues = []struct {
	ID        int
	Name      string
	Estimate  float64
	Completed bool
}{
	{ID: 0, Name: "Fix the thing", Estimate: 0.5, Completed: false},
	{ID: 1, Name: "Unstick the widget", Estimate: 30, Completed: false},
}

var expectedUser = struct {
	Name   string
	Role   string
	Remote bool
}{Name: "Wayne Lagner", Role: "Developer", Remote: true}

func checkIssues(input string) error {
	var actual []Issue
	if err := json.Unmarshal([]byte(input), &actual); err != nil {
		return err
	}
	if len(actual) != len(expectedIssues) {
		return fmt.Errorf("issuelist: expected %d issues, got %d", len(expectedIssues), len(actual))
	}
	for i, expected := range expectedIssues {
		prefix := fmt.Sprintf("issueList[%d]", i)
		if err := checkInt(prefix+".id", actual[i].ID, expected.ID); err != nil {
			return err
		}
		if err := checkString(prefix+".name", actual[i].Name, expected.Name); err != nil {
			return err
		}
		if err := checkFloat(prefix+".estimate", actual[i].Estimate, expected.Estimate); err != nil {
			return err
		}
		if err := checkBool(prefix+".completed", actual[i].Completed, expected.Completed); err != nil {
			return err
		}
	}
	return nil
}

func checkUser(input string) error {
	var actual User
	if err := json.Unmarshal([]byte(input), &actual); err != nil {
		return err
	}
	if err := checkString("userObject.name", actual.Name, expectedUser.Name); err != nil {
		return err
	}
	if err := checkString("userObject.role", actual.Role, expectedUser.Role); err != nil {
		return err
	}
	if err := checkBool("userObject.remote", actual.Remote, expectedUser.Remote); err != nil {
		return err
	}
	return nil
}

func checkInt(field string, actual *int, expected int) error {
	if actual == nil {
		return fmt.Errorf("%s: expected %d, got missing field", field, expected)
	}
	if *actual != expected {
		return fmt.Errorf("%s: expected %d, got %d", field, expected, *actual)
	}
	return nil
}

func checkString(field string, actual *string, expected string) error {
	if actual == nil {
		return fmt.Errorf("%s: expected %q, got missing field", field, expected)
	}
	if *actual != expected {
		return fmt.Errorf("%s: expected %q, got %q", field, expected, *actual)
	}
	return nil
}

func checkFloat(field string, actual *float64, expected float64) error {
	if actual == nil {
		return fmt.Errorf("%s: expected %v, got missing field", field, expected)
	}
	if *actual != expected {
		return fmt.Errorf("%s: expected %v, got %v", field, expected, *actual)
	}
	return nil
}

func checkBool(field string, actual *bool, expected bool) error {
	if actual == nil {
		return fmt.Errorf("%s: expected %t, got missing field", field, expected)
	}
	if *actual != expected {
		return fmt.Errorf("%s: expected %t, got %t", field, expected, *actual)
	}
	return nil
}

func TestIsValidJSON(t *testing.T) {
	type testCase struct {
		name      string
		input     string
		checkFunc func(string) error
	}

	runCases := []testCase{
		{
			name:      "issueList",
			input:     issueList,
			checkFunc: checkIssues,
		},
	}

	submitCases := append(runCases, []testCase{
		{
			name:      "userObject",
			input:     userObject,
			checkFunc: checkUser,
		},
	}...)

	testCases := runCases
	if withSubmit {
		testCases = submitCases
	}

	skipped := len(submitCases) - len(testCases)

	passed := 0
	failed := 0

	for _, test := range testCases {
		if err := test.checkFunc(test.input); err != nil {
			failed++
			t.Errorf(`---------------------------------
Test Failed. %s:
%v
  =>
actual error: %v
`,
				test.name, test.input, err)
			continue
		}

		passed++
		fmt.Printf(`---------------------------------
Test Passed. %s:
%v
`, test.name, test.input)
	}
	fmt.Println("---------------------------------")
	if skipped > 0 {
		fmt.Printf("%d passed, %d failed, %d skipped\n", passed, failed, skipped)
	} else {
		fmt.Printf("%d passed, %d failed\n", passed, failed)
	}

}

// withSubmit is set at compile time depending
// on which button is used to run the tests
var withSubmit = true
