"""
Dictionaries are container types too, but they map keys to values, so their type hints include both:

item_counts: dict[str, int] = {
    "Wooden Arrow": 30,
    "Small Amethyst": 2,
}

The first type is for the keys; the second is for the values.

dict[key_type, value_type]

So dict[str, int] means:

The keys are strings
The values are integers
Not all types can be used as dictionary keys. The key types that you'll see most often are strings and integers. Dictionary values, on the other hand, can be any type.

Assignment
Fantasy Quest also tracks how many of each item a character has in their inventory. Add type hints to the get_item_count function.

Add a dict[str, int] type hint to the item_counts parameter.
Add a str type hint to the item_name parameter.
Add an int return type hint.
Don't change the function body.
"""

def get_item_count(item_counts: dict[str, int], item_name: str) -> int:
    if item_name in item_counts:
        return item_counts[item_name]
    return 0
