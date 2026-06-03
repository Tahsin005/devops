"""When to Inherit
Inheritance is a powerful tool, but do not overuse it (looking at you, Java devs). The rule of thumb is:

A should only inherit from B if A is always a B.

For example:

Cat should inherit from Animal because a cat is always an animal.
Truck should inherit from Vehicle because a truck is always a vehicle.
Lane should inherit from BadDotaPlayers because Lane is always bad at DotA.
But these are not true, and you'll end up with a mess if you try to force them:

Cat should not inherit from Dog because a cat is not always a dog.
Animal should not inherit from Cat because an animal is not always a cat.
Allan should not inherit from Employed because Allan is not always employed.
When a child class inherits from a parent, it inherits everything. If you only want to share some functionality, inheritance should not be the tool you use. Just share some functions, or maybe make a new parent class that both classes can inherit from.
"""