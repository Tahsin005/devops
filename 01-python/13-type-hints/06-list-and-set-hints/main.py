"""
List and Set Hints
We've covered hints for basic types like str, int, float, and bool, but you can also add hints for container types: types that hold other values. For example:

list: mutable sequence of values
set: unordered collection of unique values
dict: collection of key-value pairs
tuple: immutable sequence of values
When we type-hint a container, we specify what kind of container it is and what type of values it contains. For example, a list of strings can be expressed as list[str]:

inventory: list[str] = ["Iron Sword", "Healing Potion"]

The "contained" type goes in square brackets after the container type. Similarly, for a set of strings, we would write set[str]:

unique_items: set[str] = {"Iron Sword", "Healing Potion"}

Assignment
Fantasy Quest has a function that removes duplicate item names from a character's inventory. It works correctly but lacks annotation. Add type hints to get_unique_items.

Add a list[str] type hint to the inventory parameter.
Add a set[str] return type hint.
Don't change the function body.
"""

def get_unique_items(inventory: list[str]) -> set[str]:
    unique_items = set()

    for item in inventory:
        unique_items.add(item)

    return unique_items
