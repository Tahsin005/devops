"""
Multiple Objects
Remember, an object is an "instance" of a class.

In object-oriented programming, an instance is a concrete occurrence of any object... "Instance" is synonymous with "object" as they are each a particular value... "Instance" emphasizes the distinct identity of the object. The creation of an instance is called instantiation.

-- Wikipedia

I can create a Wall class (you can think of a class as a "blueprint" or a "template" for an object) like this:

class Wall:
    def __init__(self, depth, height, width):
        self.depth = depth
        self.height = height
        self.width = width

Then I can create three different "instances" of the class. Or, in other words, I can create three separate objects, each with their own properties independent of each other:

wall_maria = Wall(1, 2, 3)
wall_rose = Wall(4, 5, 6)
wall_sina = Wall(9, 8, 7)

Assignment
Take a look at the Brawler class and the fight function provided, then complete the main function by doing the following:

Create 4 new brawlers with the following stats:
Name: Aragorn. Speed: 4. Strength: 4.
Name: Gimli. Speed: 2. Strength: 7.
Name: Legolas. Speed: 7. Strength: 7.
Name: Frodo. Speed: 3. Strength: 2.
Call fight twice:
The first fight should be Aragorn (attacker) vs Gimli (defender).
The second will be Legolas (attacker) vs Frodo (defender).
"""


def main():
    brawlers = [
        Brawler("Aragorn", 4, 4),
        Brawler("Gimli", 2, 7),
        Brawler("Legolas", 7, 7),
        Brawler("Frodo", 3, 2),
    ]
    fight(brawlers[0], brawlers[1])
    fight(brawlers[2], brawlers[3])

class Brawler:
    def __init__(self, name, speed, strength):
        self.name = name
        self.speed = speed
        self.strength = strength
        self.power = speed * strength


def fight(attacker, defender):
    print(f"{attacker.name}: {attacker.power} power")
    print(f"{defender.name}: {defender.power} power")
    if attacker.power > defender.power:
        print(f"{attacker.name} wins!")
    elif attacker.power < defender.power:
        print(f"{defender.name} wins!")
    else:
        print("It's a tie!")
    print("---------------------------------")


main()
