"""
Function Parameters
Function parameters can have type hints too! The syntax is the same as variable type hints: put a colon after the parameter name, then the type.

def greet_player(name: str):
    print(f"Welcome, {name}!")

When a function has multiple parameters, each one can have its own type hint:

def add_gold(current_gold: int, found_gold: int):
    return current_gold + found_gold

While adding a type hint to a variable declaration like:

character_health: float = 72.5

is considered a bit redundant due to type inference, adding type hints to function parameters is not redundant. If you don't add them, your tooling won't know what types the function expects, which makes autocomplete and error checking less effective.

Hover your cursor over the status variable. See how the tooltip can show you that it's a string? That's what makes type hinting useful! Note that name, level, health, and magic are all "unknown" because Python can't infer function parameter types without hints.

Assignment
Fantasy Quest's character status function already works, but its parameters aren't labeled yet. Add type hints to the parameters of get_character_status.

Add a str type hint to name.
Add an int type hint to level.
Add a float type hint to health.
Add a bool type hint to has_magic.
Don't change the function body.
"""

def get_character_status(name: str, level: int, health: float, has_magic: bool) -> None:
    status = f"{name} is level {level} with {health} HP"

    if has_magic:
        status += ", and can cast spells"
    else:
        status += ", and cannot cast spells"

    return status
