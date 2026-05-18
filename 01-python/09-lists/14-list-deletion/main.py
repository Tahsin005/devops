"""
List Deletion
Python has a built-in keyword del that deletes items from objects. In the case of a list, you can delete specific indexes or entire slices.

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# delete the fourth item
del nums[3]
print(nums)
# Output: [1, 2, 3, 5, 6, 7, 8, 9]

# delete the second item up to (but not including) the fourth item
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del nums[1:3]
print(nums)
# Output: [1, 4, 5, 6, 7, 8, 9]

# delete all elements
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del nums[:]
print(nums)
# Output: []

Assignment
In Fantasy Quest there is a list of strongholds on the map that players can visit to defeat powerful bosses. Let's update the trim_strongholds function to:

Delete the first stronghold from the list
Delete the last two strongholds from the list
"""

def trim_strongholds(strongholds):
    del strongholds[0]
    del strongholds[-2:]
