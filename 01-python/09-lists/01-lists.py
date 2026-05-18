"""
Lists
A natural way to organize and store data is in a List. Some languages call them "arrays", but in Python we just call them lists. Think of all the apps you use and how many of the items in the app are organized into lists.

For example:

An X (formerly Twitter) feed is a list of posts
An online store is a list of products
The state of a chess game is a list of moves
This list is a list of things that are lists
Lists in Python are declared using square brackets, with commas separating each item:

inventory = ["Iron Breastplate", "Healing Potion", "Leather Scraps"]

Lists can contain items of any data type, in our example above we have a List of strings.

Assignment
Let's work on Fantasy Quest's inventory! We can store items the player is carrying in a list!

Fix our get_inventory function by adding Shortsword to the end of the list.
"""

def get_inventory():
    return ["Healing Potion", "Leather Scraps", "Iron Helmet", "Shortsword"]

def test():
    inventory = get_inventory()
    print(f"Inventory contains: {inventory}")
    print("=====================================")


def main():
    test()


main()
