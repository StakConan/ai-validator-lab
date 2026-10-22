text = "X-DSPAM-Confidence:    0.8475"
score = float(text[text.find(":") + 1:].strip())
print(f"score = {score}")