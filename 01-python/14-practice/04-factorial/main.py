"""
Factorial
A factorial is the product (multiplication result) of all positive integers less than or equal to a given number. For example:

1! = 1 = 1
2! = 2 * 1 = 2
3! = 3 * 2 * 1 = 6
4! = 4 * 3 * 2 * 1 = 24
5! = 5 * 4 * 3 * 2 * 1 = 120
There's also a special case for zero:

0! = 1
It's just 1 by definition of the fancy math folks (ivory tower types).

Assignment
Complete the factorial() function. It should return the factorial of a given number.

In mathematics, the ! symbol denotes a factorial, but is not a valid Python Factorial operator. Use a loop and multiplication to compute the proper result.
"""

def factorial(num: int):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result
