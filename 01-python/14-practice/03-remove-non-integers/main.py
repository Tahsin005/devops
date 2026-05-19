"""
Remove Non-Integers
The built-in type() function can be used to get the type of a variable. For example:

type(1) == int
# True

type("1") == str
# True

type(1.0) == float
# True

type("seventy-six") == int
# False

Assignment
Complete the remove_nonints() function. It takes a list and returns a new list but with all the non-integer types removed.

new_list = remove_nonints(["1", 1, "3", "400", 4, 500])
print(new_list)
# [1, 4, 500]

Do not change the input nums list. Return a new list with only the integers.
"""

def remove_nonints(nums: list) -> list[int]:
    new_list = []
    for num in nums:
        if type(num) == int:
            new_list.append(num)
    return new_list
