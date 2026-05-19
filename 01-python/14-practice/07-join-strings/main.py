"""
Join Strings
Remember, in Python the + operator can be used to concatenate (smoosh) strings together. For example:

print("hello" + " " + "world")
# hello world

author = "Tolkien"
message = "The " + "world never deserved " + author
print(message)
# The world never deserved Tolkien

Assignment
Complete the join_strings() function. It takes a list of strings and returns a new single string. The new string is the concatenation of all the input strings from the list end-to-end, in order, with a comma between them. If the list is empty, return an empty string.

For example:

string_list = ["Annie", "Reiner", "Bertholdt"]
joined_string = join_strings(string_list)
print(joined_string)
# "Annie,Reiner,Bertholdt"

string_list = ["Eren", "Mikasa", "Armin"]
joined_string = join_strings(string_list)
print(joined_string)
# "Eren,Mikasa,Armin"

Do not use the built-in .join() method... we're trying to learn how this works manually.

You shouldn't have commas at the beginning or end of the final string.
Remember, you can use negative indexes to slice strings just like you can with lists.
"""

def join_strings(strings: list[str]) -> str:
    result = ""
    for string in strings:
        result += string + ","
    return result[:-1]