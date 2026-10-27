import json

filename = input("Enter the filename: ")
try:
    f = open("week2/" + filename, encoding="utf-8")
except FileNotFoundError:
    print("File not found")
    quit()
with f:
    try:
        data = json.load(f)
    except json.JSONDecodeError:
        print("Invalid JSON format")
        quit()
    
    model = data.get("model", "N/A")
    answer = data.get("response", "N/A")
    tokens = data.get("eval_count")
    eval_ns = data.get("eval_duration")
    total_ns = data.get("total_duration")
    
    if tokens is None or not eval_ns:
        speed = None
    else:
        speed = tokens / (eval_ns / 1_000_000_000)
    
    tokens_text = tokens if tokens is not None else "N/A"
    speed_text = f"{speed:.2f} tokens/s" if speed is not None else "N/A"
    total_text = f"{total_ns / 1_000_000_000:.1f} s" if total_ns is not None else "N/A"
    
    print(f"Model: {model}")
    print(f"Answer: {answer}")
    print(f"Tokens: {tokens_text} | Speed: {speed_text} | Total: {total_text}")

summary = {
    "model": model,
    "answer": answer,
    "tokens": tokens,
    "tokens_per_second": round(speed, 2) if speed is not None else None,
}
with open("week2/summary.json", "w", encoding="utf-8") as f:
    json.dump(summary, f, indent=2, ensure_ascii=False)       # dict → ghi file