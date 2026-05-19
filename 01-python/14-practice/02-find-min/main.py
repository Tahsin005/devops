"""
Find Min
In this problem you'll need a way to represent the largest possible number: infinity. In Python, you can use this constant to represent positive infinity:

my_infinity = float("inf")

Assignment
Write a function called find_min() that finds the smallest number in a list. If the list is empty, return float("inf"). For example:

find_min([1, 3, -1, 2]) -> -1
find_min([18, 3, 7, 2]) -> 2
Do not use the built-in min() function.

Tips
Create a variable to store theww "smallest number so far". Start with float("inf") (which is the largest possible number).
Iterate over the numbers in the list.
If the current number is less than the "smallest number so far", update the "smallest number so far" to the current number.
Return the "smallest number so far" after the loop completes.
"""

def find_min(nums: list[int]) -> int | float:
    if not nums:
        return float("inf")
    
    min_so_far = float("inf")
    
    for num in nums:
        if num < min_so_far:
            min_so_far = num
            
    return min_so_far
