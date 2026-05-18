"""
Modulo Operator in Python

Find the Remainder:
The modulo operator can be used to find the remainder after a division operation. For example, 7 modulo 2 would be 1, because 2 can be multiplied evenly into 7 at most 3 times:

2 * 3 = 6

Then there is 1 remaining to get from 6 to 7.

7 - 6 = 1

The modulo operator is the percent sign: %. It's important to recognize modulo is not a percentage though! That's just the symbol we're using.

remainder = 8 % 3
# remainder = 2

An odd number is a number that when divided by 2, the remainder is not 0.

Assignment
Inside the loop in the get_odd_numbers function, use the modulo operator to check if each number, i, is odd. If a number is odd, append it to the odd_numbers list. The function already returns the odd_numbers list for you. num is an integer.
"""

def get_odd_numbers(num):
    odd_numbers = []

    for i in range(0, num):
        if i % 2 != 0:
            odd_numbers.append(i)

    return odd_numbers
