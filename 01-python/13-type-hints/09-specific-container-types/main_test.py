from main import get_reward_summary

TestCase = tuple[list[str], dict[str, int], tuple[str, int]]

run_cases: list[TestCase] = [
    (
        ["Master Key", "Jadeite Gwethdesuan"],
        {"Master Key": 1, "Jadeite Gwethdesuan": 3},
        ("Master Key", 4),
    ),
    (
        ["Poison Arrow", "Ruby-Hilted Dagger"],
        {"Poison Arrow": 30, "Ruby-Hilted Dagger": 2},
        ("Poison Arrow", 32),
    ),
]

submit_cases: list[TestCase] = run_cases + [
    (
        ["Torch", "Rope", "Iron Key"],
        {"Torch": 2, "Rope": 1, "Iron Key": 1},
        ("Torch", 4),
    ),
]

expected_annotations = {
    "items": list[str],
    "item_counts": dict[str, int],
    "return": tuple[str, int],
}


def test(
    items: list[str], item_counts: dict[str, int], expected_summary: tuple[str, int]
) -> bool:
    print("---------------------------------")
    print(f"Items: {items}")
    print(f"Item counts: {item_counts}")
    print()

    actual_summary = get_reward_summary(items, item_counts)

    print(f"Expected summary: {expected_summary}")
    print(f"Actual summary:   {actual_summary}")
    print()

    if actual_summary != expected_summary:
        print("Fail")
        return False

    for annotation_name, expected_type in expected_annotations.items():
        actual_type = get_reward_summary.__annotations__.get(annotation_name)

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
