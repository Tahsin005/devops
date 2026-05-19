from main import summarize_quest_rewards

TestCase = tuple[list[str], dict[str, int], list[tuple[str, int]]]

run_cases: list[TestCase] = [
    (
        ["Defeat the Goblin King", "Rescue the Blacksmith"],
        {"Defeat the Goblin King": 500, "Rescue the Blacksmith": 250},
        [("Defeat the Goblin King", 500), ("Rescue the Blacksmith", 250)],
    ),
    (
        ["Find the Lost Tome", "Unknown Quest"],
        {"Find the Lost Tome": 300},
        [("Find the Lost Tome", 300)],
    ),
]

submit_cases: list[TestCase] = run_cases + [
    (
        ["Light the Beacon", "Seal the Rift", "Feed the Cat"],
        {"Light the Beacon": 150, "Seal the Rift": 800},
        [("Light the Beacon", 150), ("Seal the Rift", 800)],
    ),
]

expected_annotations = {
    "completed_quests": list[str],
    "quest_rewards": dict[str, int],
    "return": list[tuple[str, int]],
}


def test(
    completed_quests: list[str],
    quest_rewards: dict[str, int],
    expected_summary: list[tuple[str, int]],
) -> bool:
    print("---------------------------------")
    print(f"Completed quests: {completed_quests}")
    print(f"Quest rewards: {quest_rewards}")
    print()

    actual_summary = summarize_quest_rewards(completed_quests, quest_rewards)

    print(f"Expected summary: {expected_summary}")
    print(f"Actual summary:   {actual_summary}")
    print()

    if actual_summary != expected_summary:
        print("Fail")
        return False

    for annotation_name, expected_type in expected_annotations.items():
        actual_type = summarize_quest_rewards.__annotations__.get(annotation_name)

        print(f"{annotation_name}: expected {expected_type}")
        print(f"{annotation_name}: actual {actual_type}")
        print()

        if actual_type != expected_type:
            print("Fail")
            return False

    print("Pass")
    return True


def main() -> None:
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases: list[TestCase] = submit_cases

if "__RUN__" in globals():
    test_cases = run_cases

main()
