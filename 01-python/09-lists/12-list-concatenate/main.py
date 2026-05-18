"""
List Operations - Concatenate
Concatenating two lists (smushing them together) is easy in Python, just use the + operator.

total = [1, 2, 3] + [4, 5, 6]
print(total)
# Prints: [1, 2, 3, 4, 5, 6]

Assignment
Fantasy Quest allows users to keep lists of their favorite items. Your job is to finish the concatenate_favorites function. It takes three different lists - the player's favorite_weapons, favorite_armor and favorite_items.

Create a new list that combines the lists favorite_weapons, favorite_armor, and favorite_items in this order.
Return the list containing the combined favorites.
"""

def concatenate_favorites(favorite_weapons, favorite_armor, favorite_items):
    return favorite_weapons + favorite_armor + favorite_items
