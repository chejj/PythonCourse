import ast
import inspect
from main import check_attacks

source = inspect.getsource(check_attacks)
tree = ast.parse(source)

assert any(isinstance(node, ast.ListComp) for node in ast.walk(tree)), \
    "Use a list comprehension instead of a for loop."
run_cases = [
    ([25, -10, 0, 40, -5, 18], [25, 40, 18]),
    ([10, 20, 30], [10, 20, 30]),
    ([-5, -2, 0], []),
]

submit_cases = run_cases + [
    ([], []),
    ([1], [1]),
    ([0], []),
    ([-1], []),
    ([5, 0, 7, -3, 12], [5, 7, 12]),
    ([-100, 50, -25, 75, 0, 10], [50, 75, 10]),
    ([3, 2, 1], [3, 2, 1]),
]

def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}")
    result = check_attacks(input1)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
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


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()