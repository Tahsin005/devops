"""
Multiple Parameters
Functions can have multiple parameters ("parameter" being a fancy word for "input"). For example, this subtract function accepts 2 parameters: a and b.

def subtract(a, b):
    result = a - b
    return result

It's the argument's position that determines which parameter receives it (at least, for now). The first argument goes to the first parameter, the second to the second, and so on. In this example, the subtract function is called with a = 5 and b = 3:

result = subtract(5, 3)
print(result)
# 2

Here's an example with four parameters:

def create_introduction(name, age, height, weight):
    first_part = "Your name is " + name + " and you are " + age + " years old."
    second_part = "You are " + height + " meters tall and weigh " + weight + " kilograms."
    full_intro = first_part + " " + second_part
    return full_intro

It can be called like this:

my_name = "John"
my_age = "30"

intro = create_introduction(my_name, my_age, "1.8", "80")
print(intro)
# Your name is John and you are 30 years old. You are 1.8 meters tall and weigh 80 kilograms.

Assignment
We need to calculate the total damage from a combo of three attacks.

Complete the triple_attack function by returning the sum of its parameters, damage_one, damage_two, and damage_three. Remember to indent the code inside the function.
"""

def triple_attack(damage_one, damage_two, damage_three):
    return damage_one + damage_two + damage_three

# This is the first triple attack
attack_one = 2
attack_two = 4
attack_three = 3
first_triple_attack_damage = triple_attack(attack_one, attack_two, attack_three)

print("Getting damage for", attack_one, attack_two, "and", attack_three, "...")
print(first_triple_attack_damage, "points of damage dealt!")
print("=====================================")

# This is the second triple attack
attack_four = -1
attack_five = 10
attack_six = 5
second_triple_attack_damage = triple_attack(attack_four, attack_five, attack_six)

print("Getting damage for", attack_four, attack_five, "and", attack_six, "...")
print(second_triple_attack_damage, "points of damage dealt!")
print("=====================================")
