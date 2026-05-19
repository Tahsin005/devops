from main import get_item_description

TestCase = tuple[str, int, bool, str]

run_cases: list[TestCase] = [
    (
        "Iron Sword",
        12,
        False,
        "Iron Sword deals 12 damage and has no magical properties",
    ),
    (
        "Crystal Staff",
        8,
        True,
        "Crystal Staff deals 8 damage and glows with arcane power",
    ),
]

submit_cases: list[TestCase] = run_cases + [
    (
        "Dragonbone Axe",
        25,
        True,
        "Dragonbone Axe deals 25 damage and glows with arcane power",
    ),
]


def test(
    item_name: str, damage: int, is_magical: bool, expected_description: str
) -> bool:
    print("---------------------------------")
    print(f"Inputs: {item_name}, {damage}, {is_magical}")
    print()

    actual_description = get_item_description(item_name, damage, is_magical)

    print(f"Expected description: {expected_description}")
    print(f"Actual description:   {actual_description}")
    print()

    if actual_description != expected_description:
        print("Fail")
        return False

    expected_type = str
    actual_type = get_item_description.__annotations__.get("return")

    print(f"Expected return type hint: {expected_type.__name__}")
    print(f"Actual return type hint:   {getattr(actual_type, '__name__', None)}")
    print()

    if actual_type is expected_type:
        print("Pass")
        return True

    print("Fail")
    return False


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
