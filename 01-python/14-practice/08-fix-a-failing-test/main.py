"""
Fix a Failing Test
We have a failing test case for our avg_luck_boost function! When an empty list is passed to the function, it should return 0.0. Instead, it tries to divide by zero and crashes.

Let's update avg_luck_boost so that all tests pass again.

Some programmers like to work this way; it's called "test-driven development" or "TDD":

Stub out a function
Write tests that expect the correct behavior
Run the tests (they should fail)
Write the function and keep updating it until it passes the tests
TDD is sometimes a controversial topic, and we won't dive into that here. But we will give you much more practice with writing tests in later courses.

Assignment
Fix the avg_luck_boost function in main.py.

At the beginning of the function, check if luck_boosts is an empty list. If so, just return 0.0 to avoid a divide-by-zero error.
"""


def avg_luck_boost(luck_boosts: list[int]) -> float:
    if not luck_boosts:
        return 0.0
    total = 0
    for boost in luck_boosts:
        total += boost
    return total / len(luck_boosts)
