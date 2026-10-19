def computegrade(score):
    if score is None or not (0.0 <= score <= 1.0):
        grade = "Bad score"
    elif score >= 0.9:
        grade = "A"
    elif score >= 0.8:
        grade = "B"
    elif score >= 0.7:
        grade = "C"
    elif score >= 0.6:
        grade = "D"
    else:
        grade = "F"
    return grade
def parse_score(score_str):
    try:
        score = float(score_str)
    except (ValueError, TypeError):
        return None
    return score
assert computegrade(0.95) == "A"
assert computegrade(0.9) == "A"
assert computegrade(0.89) == "B"
assert computegrade(0.8) == "B"
assert computegrade(0.7) == "C"
assert computegrade(0.6) == "D"
assert computegrade(0.59) == "F"
assert computegrade(0.0) == "F"
assert computegrade(1.0) == "A"
assert computegrade(1.01) == "Bad score"
assert computegrade(-0.1) == "Bad score"
assert parse_score("0.95") == 0.95
assert parse_score("abc") is None
assert computegrade(parse_score("0.95")) == "A"
assert computegrade(parse_score("abc")) == "Bad score"
assert computegrade(parse_score(None)) == "Bad score"
assert computegrade(parse_score(" ")) == "Bad score"
assert computegrade(float("nan")) == "Bad score"

print("All tests passed!")