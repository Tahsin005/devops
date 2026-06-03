"""
Inheritance
We've made it to the holy grail of object-oriented programming: inheritance.

Non-OOP languages like Go and Rust support encapsulation and abstraction... almost every language does. Inheritance, on the other hand, is typically unique to class-based languages like Python, Java, and Ruby.

What Is Inheritance?
Click to hide video

Inheritance allows a "child" class, to inherit properties and methods from a "parent" class. It's a way to share code between classes. For example, say we have this Aircraft class:

class Aircraft:
    def __init__(self, height, speed):
        self.height = height
        self.speed = speed

    def fly_up(self):
        self.height += self.speed

And say we want to also model more specific kinds of aircraft. We could create a more specific Helicopter class like this:

class Helicopter:
    def __init__(self, height, speed):
        self.height = height
        self.speed = speed
        self.direction = 0

    def fly_up(self):
        self.height += self.speed

    def rotate(self):
        self.direction += 90

Trouble is, we've rewritten a lot of the same code twice... wouldn't it be nice if a Helicopter could just take all the behavior from an Aircraft, and then just add its own unique behavior on top of that? Well, it can! We'll just make Helicopter a child class of Aircraft:

class Helicopter(Aircraft):
    def __init__(self, height, speed):
        super().__init__(height, speed)
        self.direction = 0

    def rotate(self):
        self.direction += 90

By adding Aircraft in parentheses after Helicopter, we're saying "make Helicopter a child class of Aircraft". Now Helicopter inherits all the properties and methods of Aircraft!

The super() method returns a proxy of the parent class, meaning we can use it to call the parent class's constructor and other methods. So the Helicopter's constructor says "first, call the Aircraft constructor, and then additionally set the direction property".

Now, say we want to create a Jet class. Again, because all jets are aircraft, we can inherit from Aircraft again. One parent class can have as many child classes as you want.

class Jet(Aircraft):
    def __init__(self, speed):
        # Jets always start on the ground
        super().__init__(0, speed)

    def go_supersonic(self):
        self.speed *= 2

Assignment
In Age of Dragons, all the archers are humans, but not all humans are necessarily archers. All humans have a name, but only archers have a __num_arrows property.

Complete the Archer class. It should inherit the Human class.

Its constructor should:
Call the parent constructor
Set the private __num_arrows property based on the constructor parameter
Its get_num_arrows() method should return the number of arrows the archer has.
"""

class Human:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


## don't touch above this line


class Archer(Human):
    def __init__(self, name, num_arrows):
        super().__init__(name)
        self.__num_arrows = num_arrows

    def get_num_arrows(self):
        return self.__num_arrows
