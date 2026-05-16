"""
Bitwise “&” Operator
Bitwise operators are similar to logical operators, but instead of operating on boolean values, they apply the same logic to all the bits in a value by column. For example, say you had the numbers 5 and 7 represented in binary. You could perform a bitwise AND operation and the result would be 5.

0101 is 5
0111 is 7
0101
&
0111
=
0101

A 1 in binary is the same as True, while 0 is False. So really a bitwise operation is just a bunch of logical operations that are completed in tandem by column.

0 & 0 = 0

1 & 1 = 1

1 & 0 = 0

Ampersand & is the bitwise AND operator in Python. "AND" is the name of the bitwise operation, while ampersand & is the symbol for that operation. For example, 5 & 7 = 5, while 5 & 2 = 0.

0101 is 5
0010 is 2
0101
&
0010
=
0000

Binary Notation
When writing a number in binary, the prefix 0b is used to indicate that what follows is a binary number. 0b10 is two in binary, but 10 without the 0b prefix is simply ten.

0b0101 is 5
0b0111 is 7
Putting It Together
0b0101 & 0b0111
# equals 5

binary_five = 0b0101
binary_seven = 0b0111
binary_five & binary_seven
# equals 5

Click to hide video

Guild Permissions
Sometimes applications store user permissions as binary values. If I have 4 different permissions a user can have, then I can store that as a 4-digit binary number, and if a certain bit is present, I know the permission is enabled. This can be a lot more efficient than storing entire strings.

Let's pretend we have 4 permissions related to "guilds" in Fantasy Quest ("guild" is just a fancy videogame word for "team"):

can_create_guild - Leftmost bit (0b1000)
can_review_guild - Second to leftmost bit (0b0100)
can_delete_guild - Second to rightmost bit (0b0010)
can_edit_guild - Rightmost bit (0b0001)
If a user has no permissions, their binary permissions would be 0b0000.

If a user only has the can_create_guild permission, their binary permissions would be 0b1000, but a user with can_review_guild and can_edit_guild permissions would be 0b0101.

To check for, say, the can_review_guild permission, we can perform a bitwise AND operation on the user's permissions and the enabled can_review_guild bit (0b0100). If the result is 0b0100 again, we know they have that specific permission!

user_permissions = 0b0101
can_review_guild = 0b0100

# perform bitwise AND to get the user's review permission
user_review_guild_permission = user_permissions & can_review_guild

# check if the user's review permission is equal to `can_review_guild`

Assignment
Complete each of the get_XXX_bits functions. Simply use the bitwise & operation on the input of the user's permission bits and the appropriate guild permission bits variable, and return the resulting bits for them to be checked by the tests.

4 values have been provided, use the appropriate one for each function:

can_create_guild
can_review_guild
can_delete_guild
can_edit_guild
The get_XXX_bits functions return the bits and the test code compares the result to the original permission value to see if it matches
"""

can_create_guild = 0b1000
can_review_guild = 0b0100
can_delete_guild = 0b0010
can_edit_guild = 0b0001


def get_create_bits(user_permissions):
    return user_permissions & can_create_guild


def get_review_bits(user_permissions):
    return user_permissions & can_review_guild


def get_delete_bits(user_permissions):
    return user_permissions & can_delete_guild


def get_edit_bits(user_permissions):
    return user_permissions & can_edit_guild
