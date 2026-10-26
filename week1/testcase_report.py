import csv
invalidcount = 0
tpass = 0
tfail = 0
tother = 0
high = 0
medium = 0
low = 0
pother = 0
filename = input("Enter the filename: ")
try:
    f = open("week1/" + filename, encoding="utf-8", newline="")
except FileNotFoundError:
    print("File not found")
    quit()
with f:
    reader = csv.reader(f, skipinitialspace=True)
    header = next(reader, None)      # đọc riêng dòng tiêu đề
    if header is None:
        print("File is empty")
        quit()
    for row in reader:         # mỗi row là một list
        if not row:
            continue
        for i in range(len(row)):
            row[i] = row[i].strip()  # loại bỏ khoảng trắng thừa
        if len(row) != 4:
            invalidcount += 1
            continue
        print(f"{row[0]} | {row[2]} | {row[3]}")
        status = row[3].upper()
        if status == "PASS":
            tpass += 1
        elif status == "FAIL":
            tfail += 1
        else:
            tother += 1
        priority = row[2].upper()
        if priority == "HIGH":
            high += 1
        elif priority == "MEDIUM":
            medium += 1
        elif priority == "LOW":
            low += 1
        else:
            pother += 1
    
if invalidcount > 0:
    print(f"Skipped (invalid format): {invalidcount}")
print(f"Status -> Pass: {tpass} | Fail: {tfail} | Other: {tother}")
if pother > 0:
    print(f"Priority -> High: {high} | Medium: {medium} | Low: {low} | Other: {pother}")
else:
    print(f"Priority -> High: {high} | Medium: {medium} | Low: {low}")

