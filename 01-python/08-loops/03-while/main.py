"""
While
Python has another type of loop, the while loop. It's a loop that continues while a condition remains True. The syntax is simple:

while 1:
    print("1 evaluates to True")

# prints:
# 1 evaluates to True
# 1 evaluates to True
# (...continuing)

The example above is hardcoded to continue forever, creating an infinite loop. Typically, a while loop condition is a comparison or variable, and it determines when the loop ends:

num = 0
while num < 3:
    num += 1
    print(num)

# prints:
# 1
# 2
# 3
# (the loop stops when num >= 3)

Assignment
In Fantasy Quest, player characters regenerate health when standing still while away from enemies. This means they will gain health but can't run from enemies that are coming towards them while regenerating.

Complete the regenerate function using a while loop. It takes current_health, max_health and enemy_distance integers and returns an integer.

Use a while loop to determine if they can regenerate. Assume they're stationary and enemies are pursuing them. The character can regenerate while both of these conditions are true:
The character's current_health is less than their max_health.
An enemy is more than a distance of 3 from the character.
For each iteration of the loop:
The character gains 1 health.
The enemy_distance shortens by 2.
Return the new current_health after regeneration stops.
Tip
Ensure that the return statement is placed outside the while loop to correctly return the final value after the looping ends
"""

def regenerate(current_health, max_health, enemy_distance):
    while current_health < max_health and enemy_distance > 3:
        current_health += 1
        enemy_distance -= 2
    return current_health


