"""
Counting Practice
Checking for Existence
If you're unsure whether a key exists in a dictionary, use the in keyword.

cars = {
    "ford": "f150",
    "toyota": "camry"
}

print("ford" in cars)
# Prints: True

print("gmc" in cars)
# Prints: False

Assignment
We need to report how many enemies are in our players immediate vicinity - but they want to know what those enemies are! Fix the count_enemies function. It accepts as input:

enemy_names: a list of strings
It should return a dictionary where:

The keys are all the enemy names from the list
The values are the number of times each enemy appeared in the list
Run the code in its current state. It will raise a KeyError.
Fix the code: before updating a key's value, check if the key is already in the dictionary. If it is, increment it. If it isn't, set that key to 1 to create its first entry in the dictionary.
"""

def count_enemies(enemy_names):
    enemies_dict = {}
    for enemy_name in enemy_names:
        if enemy_name not in enemies_dict:
            enemies_dict[enemy_name] = 0
        enemies_dict[enemy_name] += 1
    return enemies_dict
