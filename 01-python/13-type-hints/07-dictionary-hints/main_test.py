from main import get_item_count

TestCase = tuple[dict[str, int], str, int]

run_cases: list[TestCase] = [
    ({"Wooden Arrow": 30, "Small Amethyst": 2}, "Small Amethyst", 2),
    ({"Torch": 5, "Rope": 2}, "Rope", 2),
]

submit_cases: list[TestCase] = run_cases + [
    ({"Arrow": 30, "Mana Crystal": 4}, "Dragon Scale", 0),
]

expected_annotations = {"item_counts": dict[str, int], "item_name": str, "return": int}


def test(item_counts: dict[str, int], item_name: str, expected_count: int) -> bool:
    print("---------------------------------")
    print(f"Item counts: {item_counts}")
    print(f"Item name: {item_name}")
    print()

    actual_count = get_item_count(item_counts, item_name)

    print(f"Expected count: {expected_count}")
    print(f"Actual count:   {actual_count}")
    print()

    if actual_count != expected_count:
        print("Fail")
        return False

    for annotation_name, expected_type in expected_annotations.items():
        actual_type = get_item_count.__annotations__.get(annotation_name)

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
