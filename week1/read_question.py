try:
    f = open("week1/questions.txt", encoding="utf-8")
except FileNotFoundError:
    print("File not found")
    quit()
count = 0
with f:
    for line in f:
        line = line.strip()
        if line == "" or line.startswith("#"):
            continue
        count += 1
        print(f"Q{count}: {line}")
    print(f"Total: {count} questions")