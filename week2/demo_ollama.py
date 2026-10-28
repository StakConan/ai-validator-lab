import json
import requests

# Bước 1: Viết phiếu gọi món (một dictionary của Python)
payload = {
    "model": "llama3.2:3b",
    "prompt": "Say hello in Vietnamese.",
    "stream": False
}
print("1. Phiếu gọi món:", json.dumps(payload, ensure_ascii=False))

# Bước 2: Gửi phiếu tới bếp và chờ
response = requests.post("http://localhost:11434/api/generate", json=payload, timeout=300)
print("2. Phục vụ báo:", response.status_code)

# Bước 3: Món mang ra là một đoạn văn bản JSON
print("3. Nội dung thô:", response.text[:150], "...")
print("   Kiểu dữ liệu:", type(response.text))

# Bước 4: "Mở hộp" – chuyển văn bản JSON thành dictionary
data = response.json()
print("4. Sau khi chuyển:", type(data))

# Bước 5: Lấy đúng phần mình cần
if response.status_code == 200:
    print("5. Câu trả lời:", data["response"])
    print("   Số token:", data["eval_count"])