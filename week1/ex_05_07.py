def parse_number(text):
    try:
        number = float(text)
    except ValueError:
        return None
    if number != number or number in (float("inf"), float("-inf")):
        return None
    return number

count = 0
total = 0

while True:
    text = input("Enter a number: ")
    if text == "done":
        break
    number = parse_number(text)
    if number is None:
        print("Invalid input")
        continue
    count += 1
    total += number

if count == 0:
    print("No numbers entered")
else:
    print("total =", total, "count =", count, "average =", total / count)