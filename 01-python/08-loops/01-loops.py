"""
Loops
Loops are a programmer's best friend. Loops allow us to do the same operation multiple times without having to write it explicitly each time.

For example, let's pretend I want to print the numbers 0-9.

I could do this:

print(0)
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)

Even so, it would save me a lot of time typing to use a loop. Especially if I wanted to do the same thing one thousand or one million times.

A "for loop" in Python is written like this:

for i in range(0, 10):
    print(i)

i is a variable that takes on each value from 0 to 9, one at a time. In English, the code says:

Start with i equals 0. (i in range(0))
If i is greater than or equal to 10 (range(0, 10)), exit the loop. Else:
Print i to the console. (print(i))
Add 1 to i. (range defaults to incrementing by 1)
Go back to step 2.
The result is that the numbers 0-9 are logged to the console in order.

The numbers a, b in range(a, b) are inclusive of a and exclusive of b.
So range(0, 10) includes 0 but not 10.

Whitespace Matters in Python!
The body of a for-loop must be indented, otherwise you'll get a syntax error.

Assignment
Complete the missing sections of the for-loop in the print_numbers function so that it prints the numbers 0-99 to the console.
"""

def print_numbers():
    for i in range(100):
        print(i)

def test():
    print("Printing numbers from 0 to 99:")
    print_numbers()
    print("=====================================")


def main():
    test()


main()
