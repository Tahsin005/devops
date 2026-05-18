"""
Counting the Items in a List
Remember that we can iterate over all the elements in a list using a loop. For example, the following code will print each item in the sports list.

for i in range(0, len(sports)):
    print(sports[i])

Assignment
Our players need a way to see how many copies of a specific item they have within their inventory!

Let's finish the get_item_counts function.

Within the loop, check if the items are the strings "Potion", "Bread", or "Shortsword".
If you find a match, increment the corresponding counter, either potion_count, bread_count or shortsword_count.
Tip
The example shows you how to access the values in a list. Combine this with what you know about comparison and assignment operators to complete the assignment.
"""

def get_item_counts(items):
    potion_count = 0
    bread_count = 0
    shortsword_count = 0

    for i in range(0, len(items)):
        item = items[i]

        if item == "Potion":
            potion_count += 1
        elif item == "Bread":
            bread_count += 1
        elif item == "Shortsword":
            shortsword_count += 1

    return potion_count, bread_count, shortsword_count
