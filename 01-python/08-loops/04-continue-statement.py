"""
Continue Statement
Sometimes, while looping through a sequence, you may find items that you want to skip. Python (like many programming languages) provides a way to do this: the continue statement.

continue means "go directly to the next iteration of this loop." Whatever else was supposed to happen in the current iteration is skipped.

Let's say we want to print all the numbers from 1 to 50, but skip every 7th number. We can use continue to do this, by keeping track of a counter:

# Remember, `range` is inclusive of the start, but exclusive of the end
counter = 0
for number in range(1, 51):
    counter = counter + 1

    if counter == 7:
        counter = 0 # Reset the counter
        continue # Skip this number

    print(number)

What we'll see printed are all the numbers from 1 to 50, except for 7, 14, 21, 28, 35, 42, and 49.

Avoiding Work
A continue statement immediately halts the current iteration and jumps to the next one, which saves the program from doing unnecessary work.

For example, if we're calculating square roots, we might want to skip negative numbers. continue lets us move on to the next number without wasting any time:

for number in range(-5, 5):
    if number < 0:
        continue  # Skip negatives

    print(f"The square root of {number} is {number ** 0.5}")

This would print:

The square root of 0 is 0.0
The square root of 1 is 1.0
The square root of 2 is 1.4142135623730951
The square root of 3 is 1.7320508075688772
The square root of 4 is 2.0

Using continue to avoid pointless work can make your code run faster, which is especially helpful if the loop includes time-consuming computations.

Assignment
In Fantasy Quest, we want to grant the player an enchantment each time they complete three quests. And the higher the number of total quests completed, the stronger the enchantment.

Fix the award_enchantments function. It calculates the strength of the enchantment – 5 times the total number of quests completed – and prints a message for the player. But we need to make sure this happens only once for every three quests that we iterate over within the loop! Only count the quests in the loop, don't worry about the total number of quests being divisible by 3.

At the beginning of the function, before the loop, initialize a counter variable to 0.
Within the for loop:
Add 1 to counter in each iteration, to keep track of how many quests we've seen.
If counter is less than 3, continue to the next iteration.
Otherwise, we must have completed 3 quests! Reset counter to 0 before the enchantment is awarded.
Example:

award_enchantments(2, 8, 1)
# loop through the quests:
# 2 -> first quest: continue
# 3 -> second quest: continue
# 4 -> third quest: "Enchantment of strength 20 awarded for completing 4 quests!"
# 5 -> first quest: continue
# 6 -> second quest: continue
# 7 -> third quest: "Enchantment of strength 35 awarded for completing 7 quests!"
"""

def award_enchantments(start, end, step):
    counter = 0
    for quest_number in range(start, end, step):
        counter += 1
        if counter < 3:
            continue
        counter = 0
        enchantment_strength = quest_number * 5
        print(
            f"Enchantment of strength {enchantment_strength} awarded for completing {quest_number} quests!"
        )


def test(start, end, step):
    print(f"Testing with quests {start} through {end - 1}:")
    award_enchantments(start, end, step)
    print("========================================")


def main():
    test(1, 11, 1)
    test(20, 24, 1)
    test(10, 12, 1)
    test(11, 19, 1)


main()
