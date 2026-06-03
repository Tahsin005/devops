"""Operator Overloading
Another kind of built-in polymorphism in Python is the ability to override how an operator works. For example, the + operator works for built-in types like integers and strings.

print(3 + 4)
# 7

print("three " + "four")
# three four

Custom classes on the other hand don't have any built-in support for those operators:

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = Point(4, 5)
p2 = Point(2, 3)
p3 = p1 + p2
# TypeError: unsupported operand type(s) for +: 'Point' and 'Point'

But we can add our own support! Python uses special methods with double underscores, sometimes called "dunder methods", to hook into built-in behaviors. You've already used __init__ to customize how objects are created. If we create an __add__(self, other) method on our class, the Python interpreter will use it when instances of the class are being added with the + operator. The name of the second parameter (other in this example) is just a convention - you can use any valid parameter name. Here's an example:

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

p1 = Point(4, 5)
p2 = Point(2, 3)
p3 = p1 + p2
# p3 is (6, 8)

Now, when p1 + p2 is executed, under the hood the Python interpreter just calls p1.__add__(p2).

Assignment
In Age of Dragons, players craft new weapons from old ones. To keep this mechanic simple for other developers, we'll use operator overloading on the Sword class.

Observe how the test suite uses the + operator to craft the swords.

Create an __add__(self, other) method on the Sword class.

If two "bronze" swords are crafted together, return a new Sword of type "iron".
If two "iron" swords are crafted together, return a new Sword of type "steel".
If a player tries to craft anything other than 2 bronze swords or 2 iron swords, just raise an Exception with the message "cannot craft".
Note that a sword's sword_type is just a string, one of:

bronze
iron
steel
"""

class Sword:
    def __init__(self, sword_type):
        self.sword_type = sword_type

    def __add__(self, other):
        if self.sword_type == "bronze" and other.sword_type == "bronze":
            return Sword("iron")
        elif self.sword_type == "iron" and other.sword_type == "iron":
            return Sword("steel")
        else:
            raise Exception("cannot craft")


"""
Operator Overload Review
As we discussed in the last assignment, operator overloading is the practice of defining custom behavior for standard Python operators. Here's a list of how the operators translate into method names.

Operation	Operator	Method
Addition	+	__add__
Subtraction	-	__sub__
Multiplication	*	__mul__
Power	**	__pow__
Division	/	__truediv__
Floor Division	//	__floordiv__
Remainder (modulo)	%	__mod__
Bitwise Left Shift	<<	__lshift__
Bitwise Right Shift	>>	__rshift__
Bitwise AND	&	__and__
Bitwise OR	|	__or__
Bitwise XOR	^	__xor__
Bitwise NOT	~	__invert__
"""