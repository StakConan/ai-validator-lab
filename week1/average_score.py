def parse_number(text):
    try:
        number = float(text)
    except ValueError:
        return None
    if number != number or number in (float("inf"), float("-inf")):
        return None
    return number

def parse_confidence(text):
    pos = text.find(":")
    if pos == -1:
        return None
    score = parse_number(text[pos + 1:].strip())
    if score is None or not (0.0 <= score <= 1.0):
        return None
    return score

filename = input("Enter the filename: ")

try:
    f = open("week1/" + filename, encoding="utf-8")
except FileNotFoundError:
    print("File not found")
    quit()

scores = []
invalidcount = 0

with f:
    for line in f:
        line = line.strip()
        if line == "" or line.startswith("#"):
            continue
        score = parse_confidence(line)
        if score is None:
            invalidcount += 1
            continue
        scores.append(score)

if len(scores) == 0:
    print("No valid scores found.")
else:
    print(
        f"Valid: {len(scores)} | Invalid: {invalidcount} | Average: {sum(scores) / len(scores):.3f} | " 
        f"Max: {max(scores)} | Min: {min(scores)}"
    )