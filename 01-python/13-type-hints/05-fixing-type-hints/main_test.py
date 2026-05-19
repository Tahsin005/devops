from main import get_greeting

TestCase = tuple[str, str]

run_cases: list[TestCase] = [
    ("Gandalf", "Welcome to Fantasy Quest, Gandalf!"),
    ("Frodo", "Welcome to Fantasy Quest, Frodo!"),
]

submit_cases: list[TestCase] = run_cases + [
    ("Aragorn", "Welcome to Fantasy Quest, Aragorn!"),
]


def test(player_name: str, expected_greeting: str) -> bool:
    print("---------------------------------")
    print(f"Input: {player_name}")
    print()

    actual_greeting = get_greeting(player_name)

    print(f"Expected greeting: {expected_greeting}")
    print(f"Actual greeting:   {actual_greeting}")
    print()

    if actual_greeting != expected_greeting:
        print("Fail")
        return False

    expected_type = str
    actual_type = get_greeting.__annotations__.get("return")

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
