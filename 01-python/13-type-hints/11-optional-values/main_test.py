from main import summon_mount

TestCase = tuple[bool, int, str | None]

run_cases: list[TestCase] = [
    (True, 100, "Battle Horse"),
    (False, 67, None),
]

submit_cases: list[TestCase] = run_cases + [
    (True, 800, None),
    (True, 420, "Battle Horse"),
]

expected_annotations = {
    "has_mount": bool,
    "distance": int,
    "return": str | None,
}


def test(has_mount: bool, distance: int, expected_mount: str | None) -> bool:
    print("---------------------------------")
    print(f"Has mount: {has_mount}")
    print(f"Distance: {distance}")
    print()

    actual_mount = summon_mount(has_mount, distance)

    print(f"Expected mount: {expected_mount}")
    print(f"Actual mount:   {actual_mount}")
    print()

    if actual_mount != expected_mount:
        print("Fail")
        return False

    for annotation_name, expected_type in expected_annotations.items():
        actual_type = summon_mount.__annotations__.get(annotation_name)

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
