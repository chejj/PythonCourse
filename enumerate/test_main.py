from complete_main import number_inventory

run_cases = [
    (
        {"Ice Arrow": 5, "Ocarina": 1, "Bomb": 2},
        [
            "1. Ice Arrow x 5",
            "2. Ocarina x 1",
            "3. Bomb x 2",
        ],
    ),
    (
        {"Potion": 3},
        [
            "1. Potion x 3",
        ],
    ),
    (
        {"Sword": 1, "Shield": 1},
        [
            "1. Sword x 1",
            "2. Shield x 1",
        ],
    ),
]

submit_cases = run_cases + [
    ({}, []),
    (
        {"Health Potion": 10, "Mana Potion": 4, "Elixir": 2},
        [
            "1. Health Potion x 10",
            "2. Mana Potion x 4",
            "3. Elixir x 2",
        ],
    ),
    (
        {"Bow": 1, "Arrow": 20, "Torch": 6, "Rope": 2},
        [
            "1. Bow x 1",
            "2. Arrow x 20",
            "3. Torch x 6",
            "4. Rope x 2",
        ],
    ),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input: {input1}")
    print("Expected:")
    for line in expected_output:
        print(line)
    print("Actual:")
    number_inventory(input1)
    print()
    return True


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)

    for test_case in test_cases:
        if test(*test_case):
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


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()