"""
List Updates
We can also change the item that exists at a given index. For example, we can change Leather to Leather Armor in the inventory list in the following way:

inventory = ["Leather", "Iron Ore", "Healing Potion"]
inventory[0] = "Leather Armor"
# inventory: ['Leather Armor', 'Iron Ore', 'Healing Potion']

Assignment
Fantasy Quest is trialing a new inventory system for their hardcore game mode. If a player has Iron Ore or an Iron Bar, it is always stored in the 2nd inventory slot, and they can only have one or the other.

Let's finish the smelt_ore function:

Check if they have Iron Ore in the second inventory slot (index 1).
If they do, change it into an Iron Bar.
"""

def smelt_ore(inventory):
    if inventory[1] == "Iron Ore":
        inventory[1] = "Iron Bar"
    return inventory
