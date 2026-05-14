"""
Character Report
One of our interns built a program that prints information about Fantasy Quest characters. It's almost done, but there are still a few bugs.

Assignment
Fix the bugs to get the character report working!

Run the code to see it fail.
Fix the syntax so that each variable is the data type you'd expect:
name: String
level: Integer
character_class: String
magic_resistance: Float (keep it equal to 15 but change it to a float)
account_active: Boolean
Do not change the values themselves, only the syntax around them to change their data type.
"""

name = "Lopen"
level = 25
character_class = "Windrunner"
magic_resistance = 15.0
account_active = True

print("Character Report")
print(f"{name} is a level {level} {character_class}.")
print(f"They have {magic_resistance} magic resistance.")
print(f"Their account is currently active: {account_active}")

print("=========================")
print("Character Report Complete")
print("Data types:")
print(
    f"name: {type(name).__name__}, level: {type(level).__name__}, character_class: {type(character_class).__name__}"
)
print(f"magic_resistance: {type(magic_resistance).__name__}")
print(f"account_active: {type(account_active).__name__}")
