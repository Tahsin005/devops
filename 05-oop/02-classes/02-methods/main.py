"""
Methods
So you might be wondering why classes are useful, they're like dictionaries... but worse... Right?

Well, no. First of all, classes provide structure. The class definition says "hey, I have these specific properties". A dictionary is more powerful in the sense that you can store whatever you want in it, but that also makes it less clear what on earth is in there at any given time.

Another thing that makes classes useful is that they can have methods! A method is just a function that's tied directly to a class and has access to its properties. See the take_damage method here:

class Soldier:
    health = 5

    # This is a method that reduces the
    # health of the soldier
    def take_damage(self, damage):
        self.health -= damage

soldier_one = Soldier()
soldier_one.take_damage(2)
print(soldier_one.health)
# prints "3"

soldier_two = Soldier()
soldier_two.take_damage(1)
print(soldier_two.health)
# prints "4"

Self
Methods are defined within the class declaration. Their first parameter is always the instance of the class that the method is being called on. By convention, it's called "self", and because self is a reference to the object, you can use it to read and update the properties of the object.

Notice that methods are called directly on an object instance using the dot operator:

my_object.my_method()

Assignment
Complete the fortify() method on the wall class. It should double the current armor property.
"""

class Wall:
    armor = 10
    height = 5

    def fortify(self):
        self.armor *= 2
