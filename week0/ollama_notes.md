# Ollama – Quan sát đầu tiên (17/10/2026)

## Môi trường
- Model: llama3.1:8b | RAM máy: 16GB | RAM khi chạy: ... GB
- Tốc độ: ... tokens/s
- Context: Q1 và Q2 hỏi chung một phiên → Q2 mang theo context của Q1. Từ Q3 dùng /clear trước mỗi câu.

## Kết quả chấm
| ID | Câu hỏi | Kết quả | Mức | Ghi chú |
|----|---------|---------|-----|---------|
| Q1 | 7 testing principles | 0/7 nguyên tắc đúng | Bịa | Liệt kê 7 best practice chung về test management, trình bày tự tin, có câu rào "some sources might differ" |
| Q2 | Verification vs Validation | Ý chính đúng, có ví dụ và so sánh | Đúng | Accuracy 4, Completeness 5, Conciseness 2. Lệch nhỏ: gắn verification với tuân thủ quy trình; ví dụ "kiểm tra bản vẽ" chưa chuẩn. Hỏi chung phiên với Q1 (context 560 tokens) |
| Q3 | Boundary value analysis | Ví dụ 2-value đúng (12,13,120,121); thiếu 3-value; định nghĩa lệch; nhãn TC không nhất quán | Một phần | Acc 4, Comp 3 (2.5/4 key points), Conc 2. /clear OK (prompt 18 tokens) |
| Q4 | CT-AI authors | | | Đối chiếu PDF: tên nào bịa? |
| Q5 | Kiểm thử hồi quy (VN) | | | |

## Tổng hợp kết quả
| ID | Câu hỏi | Kết quả |
|----|---------|---------|
| Q1 | 7 testing principles | Bịa (0/7) |
| Q2 | Verification vs Validation | Đúng (lỗi nhỏ, dài dòng) |
| Q3 | Boundary value analysis | Một phần (thiếu 3-value) |
| Q4 | CT-AI authors | Từ chối trung thực (3/3) |
| Q5 | Kiểm thử hồi quy (VN) | Sai (lạc đề) |
| Q5b | Kiểm thử hồi quy, có ngữ cảnh (VN) | Bịa |
| Q5c | Regression testing (EN) | Đúng (lỗi nhỏ) |

## Rubric v2
- Đúng: đủ key points bắt buộc, KHÔNG có lỗi nghiêm trọng (lỗi nhỏ ghi ở Note)
- Một phần: thiếu key point bắt buộc, HOẶC có lỗi nghiêm trọng
- Sai / Bịa / Từ chối trung thực: giữ nguyên
- Lỗi nghiêm trọng = làm người dùng hiểu sai bản chất khái niệm

## Expected Q4 (nguồn: ISTQB CT-AI syllabus, phần Acknowledgements)
- Tác giả: ISTQB AI Taskforce, chair: Klaudia Dussa-Zieger
- Danh sách tác giả hợp lệ (v1.0 + v2.0, 8 người):
  Klaudia Dussa-Zieger, Stuart Reid, Vipul Kocher, Qin Liu,
  Kyle Alexander Siemens, Werner Henschelchen,
  Jaroslaw Hryszko (v2.0), Adam Leon Smith (v1.0)

## Expected Q5 ("Kiểm thử hồi quy là gì?")
Câu trả lời mẫu (1–2 câu):
Kiểm thử hồi quy (regression testing) là kiểm thử lại các phần KHÔNG thay đổi của hệ thống sau khi có thay đổi (sửa lỗi, thêm tính năng, đổi cấu hình hoặc môi trường), để phát hiện lỗi mới phát sinh do thay đổi đó.

Key points BẮT BUỘC:
- K1: Mục đích là phát hiện lỗi mới / tác dụng phụ do thay đổi gây ra
- K2: Kiểm tra các phần không bị thay đổi (vốn đang chạy đúng)
- K3: Được kích hoạt bởi thay đổi: code, cấu hình hoặc môi trường

Key points CỘNG ĐIỂM (không bắt buộc):
- K4: Phân biệt với confirmation testing (retest): retest kiểm tra lỗi đã sửa có hết chưa; regression kiểm tra sửa xong có làm hỏng chỗ khác không
- K5: Phạm vi xác định qua impact analysis; là ứng viên tốt cho automation vì chạy lặp lại nhiều lần

Quy tắc chấm:
- Đúng: đủ K1–K3, không có thông tin sai
- Một phần: thiếu 1 trong K1–K3, hoặc nhầm lẫn với retest
- Sai: định nghĩa sai bản chất (ví dụ: "test lại toàn bộ từ đầu")
- Bịa: đưa ra khái niệm hoặc nguồn không tồn tại

## Thí nghiệm
- Hỏi Q1 ba lần: giống/khác nhau thế nào?
- Tiếng Việt so với tiếng Anh: ...
- Q4 hỏi 3 lần (/clear mỗi lần): từ chối 3/3 → hành vi ổn định với câu này.
- Q1 vs Q4: cùng là câu model không biết, nhưng Q1 bịa còn Q4 từ chối →
  hành vi phụ thuộc loại câu hỏi; model calibration kém.

## Nhận xét chung
- Model mạnh ở: ...
- Model yếu ở: ...
- Bài học: phải viết expected dạng key points TRƯỚC khi chạy, tránh chấm theo cảm tính sau khi đọc.
