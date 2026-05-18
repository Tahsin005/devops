"""
Merge Dictionaries
Guilds can merge in Fantasy Quest. We need to be able to take two player dictionaries (representing guilds) and merge them into a single guild.

Assignment
Complete the merge function. It accepts two dictionaries as input and returns a new merged dictionary that contains all the keys and values from the input dictionaries.

There are multiple solutions that use built-in Python functions, but we'll use only loops for practice:

Create an empty dictionary to hold the new merged result
Iterate over the key/value pairs of dict1 and add them to the merged dictionary
Iterate over the key/value pairs of dict2 and add them to the merged dictionary
Return the newly merged dictionary
If a key exists in both dictionaries, the value from the second dictionary should overwrite the value from the first dictionary. Here's the example usage:

two_towers = {"Frodo": 56, "Aragorn": 10}
rotk = {"Aragorn": 100, "Gandalf": 809}
merged_dict = merge(two_towers, rotk)
print(merged_dict)
# Output: {'Frodo': 56, 'Aragorn': 100, 'Gandalf': 809}

Notice how the value for the Aragorn key was updated.
"""

def merge(dict1, dict2):
    merged_dict = {}

    for key, value in dict1.items():
        merged_dict[key] = value

    for key, value in dict2.items():
        merged_dict[key] = value

    return merged_dict
