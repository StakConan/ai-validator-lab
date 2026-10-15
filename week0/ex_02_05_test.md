# ex_02_05 – Test ex_02_05.py (Celsius → Fahrenheit)

| ID | Input (°C) | Expected (°F) | Actual | Status | Note |
|----|-----------|---------------|--------|--------|------|
| TC01 | 0 | 32.0 | 32.0 | Pass | |
| TC02 | 100 | 212.0 | 212.0 | Pass | |
| TC03 | -40 | -40.0 | -40.0 | Pass | Điểm °C = °F |
| TC04 | 30 | 86.0 | 86.0 | Pass | |
| TC05 | 37.5 | 99.5 | 99.5 | Pass | Số thập phân |
| TC06 | `abc` | Báo lỗi rõ ràng, không crash | `ValueError` + traceback | Fail | Chưa xử lý input sai |
| TC07 | `  25  ` | 77.0 | 77.0 | Pass | `float()` tự bỏ khoảng trắng |
| TC08 | (chỉ có khoảng trắng) | Báo lỗi rõ ràng, không crash | `ValueError` + traceback | Fail | Giống TC06 |
