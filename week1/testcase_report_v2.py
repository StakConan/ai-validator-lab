import csv
from itertools import count
filename = input("Enter the filename: ")
try:
    f = open("week1/" + filename, encoding="utf-8", newline="")
except FileNotFoundError:
    print("File not found")
    quit()
statuscount = {}
severitycount = {}
skipcount = 0
with f:
    reader = csv.DictReader(f, skipinitialspace=True)
    for row in reader:
        if row['Priority'] is None or row['Status'] is None:
            skipcount += 1
            continue     
        print(f"{row['ID']} | {row['Priority']} | {row['Status']}")
        statuscount[row['Status'].strip().upper()] = statuscount.get(row['Status'].strip().upper(), 0) + 1
        severitycount[row['Priority'].strip().upper()] = severitycount.get(row['Priority'].strip().upper(), 0) + 1

if skipcount > 0:
    print(f"Skipped (invalid format): {skipcount}")
part1 = []
for key, value in statuscount.items():
    part1.append(f"{key}: {value}")
print("Status -> " + " | ".join(part1))
part2 = []
for key, value in severitycount.items():
    part2.append(f"{key}: {value}")
print("Priority -> " + " | ".join(part2))