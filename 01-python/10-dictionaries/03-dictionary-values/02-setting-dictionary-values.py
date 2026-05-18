"""
Setting Dictionary Values
You don't need to create a dictionary with values already inside. It is common to create a blank dictionary then populate it later using dynamic values. The syntax is the same as getting data out of a key, just use the assignment operator (=) to give that key a value.

planets = {}
planets["Earth"] = True
planets["Pluto"] = False
print(planets["Pluto"])
# Prints False

Assignment
Use the example below to answer the question:

full_names = ["jack bronson", "jill mcarty", "john denver"]

names_dict = {}
for full_name in full_names:
    # .split() returns a list of strings
    # where each string is a single word from the original
    name_parts = full_name.split()

    # here we update the dictionary
    names_dict[name_parts[0]] = name_parts[1]

print(names_dict)
# Prints: {'jack': 'bronson', 'jill': 'mcarty', 'john': 'denver'}
"""

# Which is the correct syntax to create a new key/value pair in an existing dictionary?
# dictionary_name[new_key] = value


