"""Multiple Children
So far we've worked with linear class inheritance, but usually, inheritance hierarchies form trees, not lines. A parent class can have multiple children.



Assignment
Ensure the following requirements from the game designers are completed:

Archer should inherit from Hero.
Archer should set up the hero's name and health.
Add a private "number of arrows" variable that can be set by the constructor.
Complete the shoot method. It takes a target hero as input.
If there are no arrows left, raise a not enough arrows exception.
Otherwise, remove an arrow and deal 10 damage to the target hero.
"""

class Hero:
    def __init__(self, name, health):
        self.__name = name
        self.__health = health

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def take_damage(self, damage):
        self.__health -= damage

class Archer(Hero):
    def __init__(self, name, health, num_arrows):
        super().__init__(name, health)
        self.__num_arrows = num_arrows

    def shoot(self, target):
        if self.__num_arrows == 0:
            raise Exception("not enough arrows")
        self.__num_arrows -= 1
        target.take_damage(10)
