"""
Fix Code With Type Hints
When type hints and code behavior disagree, one of them is wrong.

If you know that you've properly typed a function signature, you can use it as the "source of truth," or as a clue for how the implementation should work.

Assignment
Fix the body of summarize_quest_rewards. It should return a list of tuples, where each tuple contains:

The quest name (a string)
The XP reward for that quest (an integer)
Currently, it adds the XP integer only, instead of the full tuple.

Don't change the function signature.
"""

def summarize_quest_rewards(
    completed_quests: list[str], quest_rewards: dict[str, int]
) -> list[tuple[str, int]]:
    summary: list[tuple[str, int]] = []

    for quest_name in completed_quests:
        if quest_name in quest_rewards:
            quest_xp = quest_rewards[quest_name]
            summary.append((quest_name, quest_xp))

    return summary
