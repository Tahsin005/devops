"""
Debugging
When you're working as a professional developer, you'll typically write code on your computer and test it by yourself before it's deployed to users.

That first part of the process is called debugging. You write some code, run it, and if it doesn't work, you fix the bugs. You repeat this process until you're confident that your code works as expected.

Complete the take_magic_damage function. It should return the new health after calculating how much magic-type damage the player takes. Here is a description of the parameters:

health: The player's starting health
resist: The player's magic resistance. This reduces the damage they take by a static amount
amp: The attacker's magic amplification. This increases the damage they deal by a multiplier
spell_power: The base damage of the spell
First, calculate the total maximum damage to be inflicted by multiplying the spell_power by the amp. Then, subtract the resist from the total damage to get the actual damage dealt. Apply that damage to the player's health and return the new health.
"""

def take_magic_damage(health, resist, amp, spell_power):
    total_max_damage = spell_power * amp
    total_max_damage -= resist
    health -= total_max_damage
    return health
