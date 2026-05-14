"""
NoneType Variables
Not all variables have a value. We can make an "empty" variable by setting it to None. None is a special value in Python that represents the absence of a value. It is not the same as zero, False, or an empty string.

my_mental_acuity = None

The value of my_mental_acuity in this case is None until we use the assignment operator, =, to give it a value.

None Is NOT a String
NoneType is not the same as a string with a value of "None":

my_none = None # this is a None-type
my_none = "None" # this is a string with the value "None"

Assignment
Declare a variable named enemy and set it to None. Don't change the print() function.
"""

enemy = None

print(enemy is None)


"""
None keyword is used to define an "empty" variable.

So when would you use it? One use case is to represent that a value hasn't been determined yet, for example, an uncaptured input. Maybe your program is waiting for a user to enter their name. You might start with a variable:

username = None

Then later in the code, once the user has entered their name, you can assign it to the username variable:

username = input("What's your name? ")

Remember, it's crucial to recognize that None is not the same as the string "None". They look the same when printed to the console, but they are different data types. If you use "None" instead of None, you will end up with code that looks correct when it's printed but fails the tests. In that case, printing the type would distinguish between the two values.

str_none = "None"
actual_none = None

print(str_none) # None
print(actual_none) # None

print(type(str_none)) # <class 'str'>
print(type(actual_none)) # <class 'NoneType'>
"""

# Why might you use a None value?

# as a default value that will be replaced later