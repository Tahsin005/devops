"""
Fixing Type Hints
The whole point of type hints is that they should match what the code actually does. If a function returns a string, its return type hint should also be str.

def get_quest_reward(quest_name: str, quest_xp: int) -> str:
    return f"You've earned {quest_xp} XP for completing the {quest_name} quest!"

An incorrect type hint is confusing at best, even if you can still force the Python code to run. Your editor will likely also warn you, with something like a red squiggly line, if a function returns a value that doesn't match its return type hint.



Assignment
Fantasy Quest's greeting function works, but its return type hint is wrong.

Fix the return type hint on get_greeting by changing it to str. Don't change the function body.

Notice that the squiggly warning goes away when the types match up!
"""

def get_greeting(player_name: str) -> str:
    return f"Welcome to Fantasy Quest, {player_name}!"
