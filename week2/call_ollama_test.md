# call_ollama.py – Test evidence (28/10/2026)

   | ID | Kịch bản | Expected | Actual | Status |
   |----|----------|----------|--------|--------|
   | TC01 | Câu hỏi bình thường: "What is regression testing? Answer in 2 sentences." | In đủ 3 dòng Model, Answer, Tokens \| Speed \| Total | Model: llama3.2:3b<br>Answer: Regression testing is a software testing process that involves re-examining a software application after changes have been made to ensure that no new bugs or defects have been introduced and that the existing functionality still works as expected. The goal of regression testing is to identify and fix any regressions or defects that may have been introduced during the development process, thereby maintaining the quality and reliability of the software.<br>Tokens: 78 \| Speed: 23.96 tokens/s \| Total: 3.8 s | Pass |
   | TC02 | Sai tên model | API Error 404: {"error":"model 'llama9:xyz' not found"} | API Error 404: {"error":"model 'llama9:xyz' not found"} | Pass |
   | TC03 | Ollama không chạy | Cannot connect to Ollama. Is it running? | Cannot connect to Ollama. Is it running? | Pass |
   | TC04 | Quá thời gian chờ | Request timed out | Request timed out | Pass |
   | TC05 | Câu hỏi rỗng | Question cannot be empty | Question cannot be empty | Pass |
