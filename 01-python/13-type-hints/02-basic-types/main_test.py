import main as student_code

TestCase = tuple[str, object, type]

run_cases: list[TestCase] = [
    ("character_name", "Gandalf", str),
    ("character_level", 80, int),
]

submit_cases: list[TestCase] = run_cases + [
    ("character_health", 99.5, float),
    ("has_magic", True, bool),
]


def test(var_name: str, expected_value: object, expected_type: type) -> bool:
    print("---------------------------------")
    print(f"Checking {var_name}")
    print()

    actual_value = getattr(student_code, var_name)
    actual_type = student_code.__annotations__.get(var_name)

    print(f"Expected value: {expected_value}")
    print(f"Actual value:   {actual_value}")
    print()

    if actual_value != expected_value:
        print("Fail")
        return False

    expected_name = expected_type.__name__
    actual_name = getattr(actual_type, "__name__", None)

    print(f"Expected type hint: {expected_name}")
    print(f"Actual type hint:   {actual_name}")
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
