"""
Find Max
Infinity
The built-in float() function can create a numeric floating point value of negative infinity. Instead of initializing a base value like 0 or -100000, we can use float("-inf") to represent negative infinity. Because every value will be greater than negative infinity, we can use it as a starting point to help us achieve our goal of finding the max value.

negative_infinity = float("-inf")
positive_infinity = float("inf")

Assignment
Our players want a way to see their strongest attack from their last combat. Some enemies may be buffed to absorb either magic or melee attacks as health, which result in negative damage. Let's add another function to analyze data from our combat log.

Complete the find_max function. It takes as input a list of integers, nums, and returns a number.

max_so_far is initialized as negative infinity.
Compare each number in nums to max_so_far. If any number is larger than max_so_far, replace max_so_far with that value.
After iterating over every number, return max_so_far. If nums is empty, return negative infinity.
Here's an example of how your find_max function should work when called:

max_val = find_max([100, 10, 22])
print(max_val)
# 100

Tip
max_so_far is just that, the highest number from the list so far. It starts as negative infinity because any and every number is larger than negative infinity.
"""

def find_max(nums):
    max_so_far = float("-inf")
    for num in nums:
        if num > max_so_far:
            max_so_far = num
    return max_so_far
