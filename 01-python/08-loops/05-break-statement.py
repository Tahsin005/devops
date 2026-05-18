"""
Break Statement
We can use continue to skip to the next iteration in a loop, but what if we want to exit the loop entirely? That's where the break statement comes in.

for n in range(42):
    print(f"{n} * {n} = {n * n}")
    if n * n > 150:
        break

# 0 * 0 = 0
# 1 * 1 = 1
# 2 * 2 = 4
# 3 * 3 = 9
# 4 * 4 = 16
# 5 * 5 = 25
# 6 * 6 = 36
# 7 * 7 = 49
# 8 * 8 = 64
# 9 * 9 = 81
# 10 * 10 = 100
# 11 * 11 = 121
# 12 * 12 = 144
# 13 * 13 = 169

This code would loop from 0 all the way to 41, but it actually exits early. Once n * n is greater than 150, the break statement executes, stopping the loop.

Assignment
When a character in Fantasy Quest is attacked, the strength of the attack is compared to the strength of the character's defensive enchantments. If the character has any enchantment that is at least as strong as the attack, then the attack is blocked and the character takes no damage.

Fix the check_defense function.

It checks each defensive enchantment against the attack. If an enchantment is strong enough, it prints that the attack is blocked. In that case, the loop should stop instead of checking further... make sure that it does!
"""

def check_defense(attack_strength, min_enchantment, max_enchantment):
    for enchantment_strength in range(min_enchantment, max_enchantment + 1):
        print(
            f"Comparing attack strength {attack_strength} to enchantment strength {enchantment_strength}."
        )

        if enchantment_strength >= attack_strength:
            print("Attack blocked!")
            break


def test(attack_strength, min_enchantment, max_enchantment):
    print(
        f"Testing attack strength {attack_strength} vs. enchantment strengths {min_enchantment}–{max_enchantment}:"
    )
    check_defense(attack_strength, min_enchantment, max_enchantment)
    print("========================================")


def main():
    test(5, 8, 12)
    test(8, 6, 10)
    test(10, 5, 8)
    test(7, 4, 7)


main()
