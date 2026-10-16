text = input("Enter a number:")
try:
    num = float(text)
except ValueError:
    print("Bad score")
    quit()
if num >= 0.9 and num <= 1.0:
    print("A")
elif num >= 0.8 and num < 0.9:
    print("B")
elif num >= 0.7 and num < 0.8:
    print("C")
elif num >= 0.6 and num < 0.7:
    print("D")
elif num < 0.6 and num >= 0.0:
    print("F")
else:
    print("Bad score")