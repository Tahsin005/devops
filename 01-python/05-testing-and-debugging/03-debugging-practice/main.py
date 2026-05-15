"""
Debugging Practice
I want to walk you through how I approach writing code, complete with all the debugging steps I take along the way.

The goal is to write small amounts of code, and then test each bit of code to make sure it's doing what we expect before moving on. Trying to write entire programs at once is a recipe for pain and suffering. The goal is to write a few lines, test them, and then write a few more lines, and repeat until you're done.

This isn't a technique that's unique to beginners. Even senior engineers write code this way.

Assignment
Let's complete the unlock_achievement function. It accepts 3 arguments:

before_xp: int
ach_xp: int
ach_name: str
It should return 2 values:

The player's xp after the achievement is unlocked (The sum of before_xp and ach_xp)
An alert message that says "Achievement Unlocked: ACHIEVEMENT_NAME", where ACHIEVEMENT_NAME is the name of the achievement
"""

def unlock_achievement(before_xp, ach_xp, ach_name):
    after_xp = before_xp + ach_xp
    alert_message = f"Achievement Unlocked: {ach_name}"
    return after_xp, alert_message
