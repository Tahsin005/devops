"""
Vowels
The anti-spam team at Fantasy Quest is doing text analysis on players' in-game chats.

Assignment
Complete the count_vowels function. It takes a string and returns:

The total number of vowels in the string (count every occurrence, not just unique)
A set of the unique vowels found in the string
We are only interested in the 5 vowels: a, e, i, o, u, and their capitalized versions. Treat uppercase and lowercase vowels as separate. For example, "A" and "a" are not the same.

Tips
Create a set of the ten vowels (both lowercase and uppercase)
Create a counter started at 0
Create an empty set to store the unique vowels
Iterate over the characters in the string, for example:
for char in text:
    # do stuff

If the character is in the set of vowels:
Increment the counter
Add the character to the set of unique vowels
Return the counter and the set of unique vowels
New Empty Set
my_new_set = set()

New Set With Values
my_new_set = {"apple", "banana", "grape"}
"""

def count_vowels(text):
    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    
    count = 0
    unique_vowels = set()
    
    for ch in text:
        if ch in vowels:
            count += 1
            unique_vowels.add(ch)
    
    return count, unique_vowels