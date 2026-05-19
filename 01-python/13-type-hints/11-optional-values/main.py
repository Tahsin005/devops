"""
Optional Values
Sometimes we work with variables that may or may not have an "actual value." For example, a character might have a damage bonus, or they might not. If they don't, we can represent that lack of value with None.

The | operator indicates that a value can be of multiple types:

damage_bonus: int | None

That means damage_bonus can be either an integer (the bonus amount) or None. For another example, a function might return a prepared spell if one is ready, or None if no spell is prepared:

def get_prepared_spell(has_spell: bool) -> str | None:
    if has_spell:
        return "Fireball"

    return None

Assignment
Fantasy Quest characters that have their own mounts can summon them, from up to a limited distance. If the character doesn't have a mount, or if the mount is too far away to be summoned, the function returns None. Add type hints to the summon_mount function.

Add a bool type hint to the has_mount parameter.
Add an int type hint to the distance parameter.
Add a str | None return type hint.
Don't change the function body.
"""

def summon_mount(has_mount: bool, distance: int) -> str | None:
    if not has_mount:
        return None

    if distance > 420:
        return None

    return "Battle Horse"
