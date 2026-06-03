"""Abstraction vs. Encapsulation Quiz
Academics love to split hairs about definitions... but in practice, we're basically talking about the same thing here.

The terms "abstraction" and "encapsulation" mostly just emphasize different aspects of the same concept:

Abstraction focuses on exposing essential features while hiding complexity
Encapsulation focuses on bundling data with methods and restricting direct access to implementation details


Creating good abstractions is particularly crucial when you're developing libraries for other developers to use. For example, the built-in pow function in Python is an abstraction that hides the complexity of calculating exponents.

pow isn't magic. Somewhere, code that does something like this exists and is called when you use pow:

def pow(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result
"""

"""
Abstraction emphasizes ____ and encapsulation emphasizes ____

-- Combining data and behavior while hiding internal implementation details / exposing the right features
"""