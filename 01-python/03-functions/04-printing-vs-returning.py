"""
Printing vs. Returning
Some new developers get hung up on the difference between print() and return.

It can be particularly confusing when the test suite we provide simply prints the output of your functions to the console. It makes it seem like print() and return are interchangeable, but they are not!

print() is a function that:
Prints a value to the console
Does not return a value
return is a keyword that:
Ends the current function's execution
Provides a value (or values) back to the caller of the function
Does not print anything to the console (unless the return value is later print()ed)
Printing to Debug Your Code
Printing values and running your code is a great way to debug your code. You can see what values are stored in various variables, find your mistakes, and fix them. Add print statements and run your code as you go! It's a great habit to get into to make sure that each line you write is doing what you expect it to do.

In the real world it's rare to leave print() statements in your code when you're done debugging. Similarly, you need to remember to remove any print() statements from your code before submitting your work here on Boot.dev because it will interfere with the tests!

Assignment
There's a problem in the get_title function! It's supposed to construct the title value and return it to the caller. Instead, it's barbarically printing the value to the console.

Fix the get_title function.

Return the title
Do not print it inside get_title
"""

def get_title(first_name, last_name, job):
    title = first_name + " " + last_name + " the " + job
    return title

def test(first_name, last_name, job):
    title = get_title(first_name, last_name, job)
    print("First name:", first_name)
    print("Last name:", last_name)
    print("Job:", job)
    print("Title:", title)
    print("=====================================")


test("Frodo", "Baggins", "warrior")
test("Bilbo", "Baggins", "thief")
test("Gandalf", "The Grey", "wizard")
test("Aragorn", "Son of Arathorn", "ranger")
