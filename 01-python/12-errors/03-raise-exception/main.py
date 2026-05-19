"""
Raising Your Own Exceptions
Errors are not something to be scared of. Every program that runs in production is expected to manage errors on a constant basis. Our job as developers is to handle the errors gracefully and in a way that aligns with our user's expectations.

Errors Are NOT Bugs
Click to hide video

When something in our own code happens that isn't the "happy path", we should raise our own exceptions. For example, if someone passes some bad inputs to a function we write, we should not be afraid to raise an exception to let them know they did something wrong.

An error or exception is raised when something bad happens, but as long as our code handles it as users expect it to, it's not a bug. A bug is when code behaves in ways our users don't expect it to.

For example, if a player tries to forge a sword out of a metal bar, we might stop that from happening by using raise to prevent a bug. If the game doesn't have certain items, such as a gold sword, then players shouldn't be able to craft a sword from gold bars even though gold bars do exist.

def craft_sword(metal_bar):
    if metal_bar == "bronze":
        return "bronze sword"
    if metal_bar == "iron":
        return "iron sword"
    if metal_bar == "steel":
        return "steel sword"
    raise Exception("invalid metal bar")

We prevent a bug by raising an exception. This exception prevents other developers who use the craft_sword function from creating items that don't exist in our game.

raise stops the program from executing and forces the exception to be handled.

Don't Catch Your Own Exceptions
As a rule of thumb, you do not want to catch exceptions you raise within the same function block, for example:

# don't do this
def craft_sword(metal_bar):
    try:
        if metal_bar == "bronze":
            return "bronze sword"
        if metal_bar == "iron":
            return "iron sword"
        if metal_bar == "steel":
            return "steel sword"
        raise Exception("invalid metal bar")
    except Exception as e:
        print(f"An error occurred: {e}")

Instead, the caller should handle any potential error by wrapping the function call within a try/except block.

# do this
try:
    craft_sword("gold bar")
except Exception as e:
    print(e)

By raising the exception instead of handling it inside craft_sword, we let the caller decide how to proceed. The caller might want to log the error, show a message to the player, or crash the program entirely.

Assignment
Fix the get_player_record function. If the given player_id doesn't exist, it currently just passes. Instead, it should raise (but not handle) an error to alert the caller that the player doesn't exist. The exception should say player id not found.

The tests will call the get_player_record function, and will handle the exception you raise.
"""

def get_player_record(player_id):
    if player_id == 1:
        return {"name": "Slayer", "level": 128}
    if player_id == 2:
        return {"name": "Dorgoth", "level": 300}
    if player_id == 3:
        return {"name": "Saruman", "level": 4000}
    raise Exception("player id not found")
