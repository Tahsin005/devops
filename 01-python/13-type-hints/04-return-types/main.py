"""
Return Types
You can also annotate the type that you expect a function to return. When you know what types go into and come out of a function, you can (probably) use it without having to read every line of the function body. Return types come after the parameter list, before the colon:

def add_gold(current_gold: int, found_gold: int) -> int:
    return current_gold + found_gold

The -> int means this function is expected to return an integer.

The syntax is a bit different from type hints on variables and parameters: we use -> instead of :, and there's no variable name before the type hint. This is because it doesn't really matter what name (if any) the function uses internally for the return value; we just care about the type.

Here's another example:

def get_greeting(player_name: str) -> str:
    return f"Welcome, {player_name}!"

The -> str means this function is expected to return a string.

Assignment
Fantasy Quest uses item descriptions in shop menus. The get_item_description function already works, and its parameters already have type hints.

Add a str return type hint to get_item_description. Don't change the function body.
"""

def get_item_description(item_name: str, damage: int, is_magical: bool) -> str:
    description = f"{item_name} deals {damage} damage"

    if is_magical:
        description += " and glows with arcane power"
    else:
        description += " and has no magical properties"

    return description
