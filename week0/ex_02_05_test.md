# ex_02_05 – Test lesson01_2.py (Celsius → Fahrenheit)

| Input (C) | Expected Result (F) | Actual result (F) | Status |
|-----------|---------------------|-------------------|--------|
| 0         | 32.0                | 32.0              | Pass   |
| 100       | 212.0               | 212.0             | Pass   |
| -40       | -40.0               | -40.0             | Pass   |
| 30        | 86.0                | 86.0              | Pass   |
| abc       | ?                   | `ValueError: could not convert string to float: 'abc'` (unhandled crash with traceback) | Fail |
| " 25 "    | 77.0                | 77.0              | Pass   |
| " "       | ?                   | `ValueError: could not convert string to float: ' '` (unhandled crash with traceback) | Fail |
