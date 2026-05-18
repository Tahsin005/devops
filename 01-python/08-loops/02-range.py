"""
Range Continued
The range() function we've been using in our for loops actually has an optional 3rd parameter: the "step".

for i in range(0, 10, 2):
    print(i)
# prints:
# 0
# 2
# 4
# 6
# 8

The "step" parameter determines how much to add to i in each iteration of the loop. You can even go backwards:

for i in range(3, 0, -1):
    print(i)
# prints:
# 3
# 2
# 1

Assignment
Fix the for loop in the count_down function. It takes start and end inputs, but start is always greater than end. It's supposed to print every integer counting down by 1, beginning at start (inclusive) and stopping just before end (exclusive), but there's a mistake in the range function call.

Tip
In the programming world, it's common for the first number in a range to be inclusive and the second number is exclusive. e.g. range(0, 10) will include:

0 1 2 3 4 5 6 7 8 9
"""

def count_down(start, end):
    for i in range(start, end, -1):
        print(i)


# Don't edit below this line


def test(start, end):
    print(f"Using inputs start: {start} and end: {end}")
    print(f"Printing numbers from {start} to {end + 1}:")
    count_down(start, end)
    print("=====================================")


def main():
    test(10, 0)
    test(20, 10)
    test(15, 11)


main()
