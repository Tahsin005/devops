"""
List Length
The length of a List can be calculated using the len() function. It takes an iterable (such as a string or list) and returns the number of items present.

fruits = ["apple", "banana", "pear"]
length = len(fruits)
# 3 items in fruits

len("supercalifragilisticexpialidocious")
# 34 characters

Don't be fooled by the fact that the length is not equal to the index of the last element. In fact, it will always be one greater because the starting index is zero!

Assignment
Some of our player's inventories are huge, so looking through the entire list is cumbersome. Let's find an easy way for us to get the index of the last item in their inventory.

Complete the get_last_index function so that it returns the length of the inventory list minus 1.
"""

def get_last_index(inventory):
    list_length = len(inventory)
    last_index = list_length - 1
    return last_index
