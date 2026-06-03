"""Polymorphism
Click to hide video

While inheritance is the most unique trait of object-oriented languages, polymorphism is probably the most powerful. It also is not particularly unique to class-based languages. Polymorphism is the ability of a variable, function or object to take on multiple forms.

"poly" = "many"
"morph" = "form"
For example, classes in the same hierarchical tree may have methods with the same name and signature but different implementations. Here's a simple example:

class Creature():
    def move(self):
        print("the creature moves")

class Dragon(Creature):
    def move(self):
        print("the dragon flies")

class Kraken(Creature):
    def move(self):
        print("the kraken swims")

for creature in [Creature(), Dragon(), Kraken()]:
    creature.move()
# prints:
# the creature moves
# the dragon flies
# the kraken swims

Because all three classes have a .move() method, we can shove the objects into a single list, and call the same method on each of them, even though the implementation (method body) is different.

This idea is sometimes referred to as "duck typing". If it looks like a duck, swims like a duck, and quacks like a duck, it's a duck. Or, in our example, if it has a .move() method, we can treat it like a Creature.

Assignment
Let's build some hit-box logic for our game, starting with a simple Rectangle.

Complete the __init__() method. Configure the class to have properties matching the variables passed into the constructor in this order:

x1
y1
x2
y2
"""

class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
