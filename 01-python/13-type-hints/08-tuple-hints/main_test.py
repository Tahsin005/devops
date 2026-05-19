from main import get_loot_drop

TestCase = tuple[int, tuple[str, int]]

run_cases: list[TestCase] = [
    (14, ("Emerald Brome", 1)),
    (3, ("Smokestone Chip", 3)),
]

submit_cases: list[TestCase] = run_cases + [
    (40, ("Emerald Brome", 1)),
    (10, ("Smokestone Chip", 3)),
]

expected_annotations = {
    "enemy_level": int,
    "return": tuple[str, int],
}


def test(enemy_level: int, expected_drop: tuple[str, int]) -> bool:
    print("---------------------------------")
    print(f"Enemy level: {enemy_level}")
    print()

    actual_drop = get_loot_drop(enemy_level)

    print(f"Expected drop: {expected_drop}")
    print(f"Actual drop:   {actual_drop}")
    print()

    if actual_drop != expected_drop:
        print("Fail")
        return False

    for annotation_name, expected_type in expected_annotations.items():
        actual_type = get_loot_drop.__annotations__.get(annotation_name)

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
