"""
Tuple Hints
Lists and sets usually hold multiple values of the same type:

inventory: list[str] = ["Black Knight Halberd", "Skull Lantern", "Notched Whip"]

But tuples are a small fixed group of values where each position has its own meaning. Because they're fixed, it's quite common for those values to be of different types. For example, a loot drop might have an item name and a quantity:

drop: tuple[str, int] = ("Garnet Mark", 2)

tuple[str, int] means:

There are two values in the tuple
The first value is a string
The second value is an integer
A tuple can have any number of values – though 2 and 3 are the most common. Here's an example representing a character's HP, MP, and stamina:

stats: tuple[int, float, int] = (100, 42.5, 75)

The type hint tuple[int, float, int] tells us this is a three-value tuple with an integer, a float, and another integer.

Assignment
Fantasy Quest uses loot drops to decide what items the player receives after defeating an enemy in battle. Add type hints to the get_loot_drop function.

Add an int type hint to the enemy_level parameter.
Add a tuple[str, int] return type hint.
Don't change the function body.
"""

def get_loot_drop(enemy_level: int) -> tuple[str, int]:
    if enemy_level > 10:
        return "Emerald Brome", 1

    return "Smokestone Chip", 3
