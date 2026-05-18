"""
Reverse List
Assignment
Some of our players would like to view their inventories in reverse order.

Using a loop, let's write a function that takes a list as an input and returns a new list except all the items are in reverse order.

For example:

[1, 2, 3] -> [3, 2, 1]
['a', 'b', 'c', 'd'] -> ['d', 'c', 'b', 'a']

Tip
The Python range function is very useful when working with lists. It allows you to choose where to start, stop, and how to step over a list.

Remember, function arguments are separated by commas inside the parentheses. For range the function signature is range(start, stop, step). Don't forget you can use negative values for these arguments!
It's common to nest built-ins: you can pass len(...) directly to range(...). For example, range(len(items)) iterates over indices 0 through len(items) - 1.
Where should you start your loop from? Could len() be useful at giving range a starting index?
Where should you end your loop?
What should the step be? In other words, how should you increment i in each iteration of the loop?
"""

def reverse_list(items):
    reversed_list = []
    for i in range(len(items) - 1, -1, -1):
        reversed_list.append(items[i])
    return reversed_list
