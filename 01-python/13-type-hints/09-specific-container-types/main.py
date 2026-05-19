"""
Specific Container Types
It's possible to type-hint a container with just the container type:

items: list = ["Black Firebomb", "Titanite Chunk"]

This says items is a list, but it doesn't tell us what kind of values go inside! Assuming you know what's inside, best to be specific:

items: list[str] = ["Black Firebomb", "Titanite Chunk"]

That said, bare container type hints aren't wrong. Sometimes you really don't know what types of values a container will hold, or the specific type hint would be too complicated to be useful. You'll see that occasionally with dicts. Just give clear type hints whenever possible!

Assignment
Fantasy Quest's reward summary function already has type hints, but some of the container types are too vague. Make the container type hints more specific.

Update items from list to list[str].
Notice that before you add the hint, the first_item variable's type tooltip is "Unknown". After you add the hint, Python can infer that first_item is a str because it's in the items list.

Update item_counts from dict to dict[str, int].
Update the function return type from tuple to tuple[str, int].
Don't change the function body.
"""

def get_reward_summary(items: list[str], item_counts: dict[str, int]) -> tuple[str, int]:
    total_items = 0

    for count in item_counts.values():
        total_items += count

    first_item = items[0]
    return first_item, total_items
