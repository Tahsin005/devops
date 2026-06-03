"""
Methods Can Return
If a normal function doesn't return anything, it's typically not a very useful function. In contrast, methods often don't return anything because they can mutate (update) the properties of the object instead. That's exactly what we did in the last assignment.

However, they can return values if you want! They're just functions with access to an object, after all. A common use case is a "getter" method that returns a calculated value based on the properties of the object.

class Soldier:
    armor = 2
    num_weapons = 2

    def get_speed(self):
        speed = 10
        speed -= self.armor
        speed -= self.num_weapons
        return speed

soldier_one = Soldier()
print(soldier_one.get_speed())
# prints "6"

Assignment
Building walls in Age of Dragons can be expensive, the larger and stronger the wall, the more it costs.

Complete the .get_cost() method on the Wall class. It should return the cost of a wall, where the cost is its armor multiplied by its height.
"""

class Wall:
    armor = 10
    height = 5

    def get_cost(self):
        return self.armor * self.height

    def fortify(self):
        self.armor *= 2
