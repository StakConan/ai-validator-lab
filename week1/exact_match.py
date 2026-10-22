def normalize(text):
    if text is None:
        return None
    return text.strip().lower()
def exact_match(answer, expected):
    if answer is None or expected is None:
        return False
    return normalize(answer) == normalize(expected)

assert normalize("  Bad Score ") == "bad score"
assert exact_match("A", "A") == True
assert exact_match("  a ", "A") == True
assert exact_match("Bad score ", "Bad score") == True
assert exact_match("B", "A") == False
assert exact_match("", "A") == False
assert exact_match(None, "A") == False
assert exact_match(None, None) == False
print(exact_match("The grade is A", "A"))
print(exact_match("Regression testing checks that changes do not break existing features",
                  "Regression testing verifies changes don't introduce defects in unchanged areas"))
print("All tests passed!")