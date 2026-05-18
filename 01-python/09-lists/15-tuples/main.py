"""
Tuples
Tuples are collections of data that are ordered and unchangeable. You can think of a tuple as a List with a fixed size. Tuples are created with round brackets:

my_tuple = ("this is a tuple", 45, True)
print(my_tuple[0])
# this is a tuple
print(my_tuple[1])
# 45
print(my_tuple[2])
# True

While it's typically considered bad practice to store items of different types in a List, it's not a problem with Tuples. Because they have a fixed size, it's easy to keep track of which indexes store which types of data.

Tuples are often used to store very small groups (like 2 or 3 items) of data. For example, you might use a tuple to store a dog's name and age.

dog = ("Fido", 4)

There is a special case for creating single-item tuples. You must include a comma so Python knows it's a tuple and not regular parentheses:

dog = ("Fido",)

Because Tuples hold their data, multiple tuples can be stored within a list. Similar to storing other data in lists, each tuple within the list is separated by a comma. When accessing a list of tuples, the first index selects which tuple you want to access, the second selects a value within that tuple.

my_tuples = [
    ("this is the first tuple in the list", 45, True),
    ("this is the second tuple in the list", 21, False)
]
print(my_tuples[0][0]) # this is the first tuple in the list
print(my_tuples[0][1]) # 45
print(my_tuples[1][0]) # this is the second tuple in the list
print(my_tuples[1][2]) # False

Tuple Unpacking
You can easily assign the values of a tuple to variables using unpacking.

dog = ("Fido", 4)
dog_name, dog_age = dog
print(dog_name)
# Fido
print(dog_age)
# 4

When you return multiple values from a function, you're actually returning a tuple.

Assignment
The Fantasy Quest character system needs a list of "heroes" to be able to run the game properly. Someone wrote some pretty nasty code, and the code in question creates a heroes list where every 3rd index defines a new hero. First their name, then their age, then whether or not they're an "elf".

Restructure the heroes list into a list of tuples by editing the syntax on lines 3 through 14, where each tuple represents one hero and contains their data in the same order.
"""

def get_heroes():
    heroes = [
        ("Glorfindel",
        2093,
        True,),
        ("Gandalf",
        1054,
        False,),
        ("Gimli",
        389,
        False,),
        ("Aragorn",
        87,
        False,),
    ]

    return heroes
