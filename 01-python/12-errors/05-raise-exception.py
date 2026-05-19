"""
try:
    raise Exception("zero division")
except ZeroDivisionError as e:
    print("zero")
"""

# In the code sample, what will happen?

# The program will crash out with an uncaught exception

"""
try:
    raise Exception("zero division")
except ZeroDivisionError as e:
    print("zero")
except Exception as e:
    print("other")
"""

# In the code sample, what will happen?

# The program will print "other"

"""
try:
    10/0
except Exception as e:
    print("other")
"""

# In the code sample, what will happen?

# The program will print "other"
