from main import get_unique_items

TestCase = tuple[list[str], set[str]]

run_cases: list[TestCase] = [
    (
        ["Iron Sword", "Healing Potion", "Iron Sword"],
        {"Iron Sword", "Healing Potion"},
    ),
    (
        ["Leather Armor", "Mage Robe", "Leather Armor", "Mage Robe"],
        {"Leather Armor", "Mage Robe"},
    ),
]

submit_cases: list[TestCase] = run_cases + [
    (
        ["Gold Coin", "Silver Ring", "Gold Coin", "Torch"],
        {"Gold Coin", "Silver Ring", "Torch"},
    ),
]

expected_annotations = {
    "inventory": list[str],
    "return": set[str],
}


def test(inventory: list[str], expected_items: set[str]) -> bool:
    print("---------------------------------")
    print(f"Inventory: {inventory}")
    print()

    actual_items = get_unique_items(inventory)

    print(f"Expected unique items: {expected_items}")
    print(f"Actual unique items:   {actual_items}")
    print()

    if actual_items != expected_items:
        print("Fail")
        return False

    for annotation_name, expected_type in expected_annotations.items():
        actual_type = get_unique_items.__annotations__.get(annotation_name)

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
