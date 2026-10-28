import json
import sys
import requests

URL_OLLAMA = "http://localhost:11434/api/generate"

def ask_ollama(prompt, model="llama3.2:3b", timeout=300):
    """Gửi câu hỏi tới Ollama. Thành công trả về dict, lỗi thì in lý do và trả về None."""
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    try:
        response = requests.post(URL_OLLAMA, json=payload, timeout=timeout)
    except requests.exceptions.Timeout:
        print("Request timed out")
        return None
    except requests.exceptions.ConnectionError:
        print("Cannot connect to Ollama. Is it running?")
        return None
    if response.status_code != 200:
        print(f"API Error {response.status_code}: {response.text}")
        return None
    try:
        return response.json()
    except json.JSONDecodeError:    
        print("Response is not valid JSON")
        return None

def summarize_response(data, save_path=None):
    """In tóm tắt phản hồi của Ollama, trả về dict tóm tắt.
    Nếu có save_path thì ghi dict đó ra file JSON."""
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

    if save_path is not None:
        with open(save_path, "w", encoding="utf-8") as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)

    return summary
if __name__ == "__main__":
    prompt = input("Nhập câu hỏi của bạn: ")
    print(".....................")    # tách hàng
    if prompt.strip() == "":
        print("Question cannot be empty")
        sys.exit()
    response_data = ask_ollama(prompt, timeout=2) # Gọi hàm sau khi nhập promt
    if response_data is None:
        print("Failed to get response from Ollama")
        sys.exit()
    summarize_response(response_data, save_path="week2/summary.json")      # dict → ghi file