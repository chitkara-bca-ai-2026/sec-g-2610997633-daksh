# 🎓 Student Lab Portfolio — BCA AI (2026 Batch)

**Student Name:** DAKSH VERMA  
**Roll Number:** `2610997633`  
**Section:** Section G  
**Batch:** BCA AI 2026 Batch  
**Repository:** `sec-g-2610997633-daksh`  

---

## 🚀 Initial Setup (One-time only)

When you start for the first time, open your terminal (Command Prompt, PowerShell, or Git Bash) and clone this repository to your laptop/system:

```bash
git clone https://github.com/chitkara-bca-ai-2026/sec-g-2610997633-daksh.git
```
*(After cloning, open the cloned folder in VS Code via **File → Open Folder**)*

---

## 📂 Repository Structure

This repository is your central coursework portfolio across lab courses. Keep your work organized inside their respective subject folders:

* **`Python/`** — Python Programming lab assignments (Labs 01 to 24) and Past Test Practice Questions.
* **`CST/`** — Client Side Technology (HTML, CSS, JS) lab exercises (Labs 01 to 13).

```text
sec-g-2610997633-daksh/
├── README.md
│
├── Python/                                  <--- [Python Programming]
│   ├── README.md                            (Complete Python coursework index)
│   ├── Lab_01/ to Lab_12/                   (Past foundation labs)
│   ├── Lab_13/                              (Inventory Control System)
│   ├── ...
│   ├── Lab_20/                              (Daily Log Book)
│   ├── Lab_21/                              (Document Statistics Tool)
│   ├── Lab_22/                              (Keyword Search Utility)
│   ├── Lab_23/                              (Student Marks File Handling Tool)
│   ├── Lab_24/                              (Student Result Analysis System - CSV)
│   └── Past_Test_Practice_Questions/        (10 Testpad practice questions & self-tests)
│
└── CST/                                     <--- [Client Side Technologies]
    ├── README.md
    ├── TASKS OF CST.pdf
    ├── Lab_01/ to Lab_13/                   (HTML, forms, tables & media labs)
```

---

## 📝 Learning & Error Log (`log.txt`) — Python Labs Only (Lab 13 Onwards)

> ⚠️ **Note:** `log.txt` is strictly required for **Python** labs starting from Lab 13. Your **CST** labs do **not** require a `log.txt` (unless your CST teacher asks for one).

For each Python lab (starting Lab 13), create a simple Notepad text file named **`log.txt`** inside that lab's folder (`Python/Lab_XX/log.txt`).

Write casually in plain words just like rough notes—record your honest thoughts, any syntax/logic bugs you encountered, and how you solved them:

### Example `log.txt`:
```text
Lab Reflection:

1. Approach:
Used a while loop to take input numbers until user entered 0, and a for loop to calculate the sum.

2. Errors Faced:
- Error 1: Infinite loop! Program kept running and didn't stop.
  Fix: Realized I forgot to increment the counter `i += 1` inside the while loop.
- Error 2: IndentationError: expected an indented block.
  Fix: Corrected 4-space tab indentation inside the loop body.

3. Output:
Tested with inputs 5, 10, 15, 0. Output printed: "Total Sum = 30".
```
*(If your code worked on the very first try without any bugs, simply write: "Ran on first attempt without errors!")*

---

## 🔄 Daily Git Commands

Whenever you add or update your code:

```bash
# 1. Stage your files
git add .

# 2. Commit your work
git commit -m "Add Python Lab 21-24 solutions, reflection logs, and practice tests"

# 3. Push to your repository
git push origin main
```

> 💡 **Multiple commits are completely fine!**  
> You can commit after each error, while trying fixes, or after completing. There is no limit on commits—multiple commits show your real problem-solving journey!
