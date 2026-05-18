"""
Pop Values
.pop() is the opposite of .append(). Pop removes the last element from a list and returns it for use. For example:

vegetables = ["broccoli", "cabbage", "kale", "tomato"]
last_vegetable = vegetables.pop()
# vegetables = ['broccoli', 'cabbage', 'kale']
# last_vegetable = 'tomato'

Assignment
Our player is selling the items in their inventory to the shopkeep! You should see a loop that iterates over each element.

Update the loop body to pop the last element into an item variable so that the code on line 19 prints the items in turn.

Note
While .pop() typically removes the last item of a list, it can also be used to remove an item at a specific index. For example, vegetables.pop(1) would remove "cabbage" from the list. This can be useful when you need to remove items from other positions in your list.
"""

def clear_inventory():
    inventory = [
        "Healing Potion",
        "Iron Bar",
        "Kite Shield",
        "Shortsword",
        "Leather Scraps",
        "Tattered Cloth",
    ]

    print(f"inventory: {inventory}")

    for i in range(0, len(inventory)):
        item = inventory.pop()

        print(f"Selling: {item}")
        print(f"inventory: {inventory}")


def test():
    clear_inventory()
    print("=====================================")


def main():
    test()


main()
