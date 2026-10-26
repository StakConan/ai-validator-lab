filename = input("Enter the filename: ")
try:
    f = open("week1/" + filename, encoding="utf-8")
except FileNotFoundError:
    print("File not found")
    quit()
invalidcount = 0
tpass = 0
tfail = 0
tother = 0
with f:
    for line in f:
        line = line.strip()
        if line == "" or line.startswith("#"):
            continue
        testcase = [x.strip() for x in line.split(",")]
        if len(testcase) != 4:
            invalidcount += 1
            continue
        
        print(f"{testcase[0]} | {testcase[2]} | {testcase[3]}")
        status = testcase[3].strip().upper()
        if status == "PASS":
            tpass += 1
        elif status == "FAIL":
            tfail += 1
        else:
            tother += 1
        if invalidcount > 0:
            print(f"Skipped (invalid format): {invalidcount}")
        print(f"Pass: {tpass} | Fail: {tfail} | Other: {tother}")
