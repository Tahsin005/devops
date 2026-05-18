"""
Even Teams
Fantasy Quest PvP teams are uneven when the match begins. We need a function that will correctly split the two teams evenly.

Assignment
Complete the get_even_and_odd_teams function.

It accepts a list of players (strings representing their names) and returns two lists in this order:

A new list of all the players with even-numbered indexes in the original list.
A new list of all the players with odd-numbered indexes in the original list.
Use the slice syntax with a "step" to create two new lists from the players list. Don't be afraid to consult your spellbook for list slicing help!
"""

def get_even_and_odd_teams(players):
    even_teams = players[::2]
    odd_teams = players[1::2]
    return even_teams, odd_teams
