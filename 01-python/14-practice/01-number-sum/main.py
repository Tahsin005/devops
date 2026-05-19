"""
Number Sum
In this chapter we are going to hammer down the concepts we've learned by running through a bunch of practice problems without introducing any new concepts.

Assignment
Complete the number_sum function. It should add up all the numbers from 1 to n and return the result. If n is less than 1, return 0. For example:

number_sum(5) -> 1+2+3+4+5 -> 15
number_sum(3) -> 1+2+3 -> 6
Remember that a range will not include the last number.
"""

def number_sum(n: int) -> int:
    if n < 1:
        return 0

    total = 0
    for num in range(1, n + 1):
        total += num
    return total
