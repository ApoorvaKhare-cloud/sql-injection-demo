# 🔐 SQL Injection Demo & Prevention (Flask Project)

## 📌 Overview
This project demonstrates a real-world web security vulnerability — **SQL Injection** — and how to prevent it using secure coding practices.

It includes:
- A vulnerable login system (can be exploited)
- A secure login system (protected using parameterized queries & hashing)

---

## 🚨 What is SQL Injection?
SQL Injection is a web security vulnerability that allows attackers to manipulate database queries by injecting malicious SQL code into input fields.

Example attack:
' OR '1'='1

This can bypass authentication without knowing the password.

---

## ⚙️ Features
- 🔴 Vulnerable Mode (demonstrates SQL Injection attack)
- 🟢 Secure Mode (prevents SQL Injection)
- 🔒 Password hashing using bcrypt
- 🎨 Clean UI using HTML & CSS
- 🧪 Hands-on demonstration of attack vs defense

---

## 🛠️ Tech Stack
- Python
- Flask
- SQLite
- Bcrypt
- HTML/CSS

---

## 🚀 How to Run

1. Clone the repository
2. Install dependencies:
   pip install flask bcrypt

3. Run database setup:
   python database.py

4. Start the server:
   python app.py

5. Open in browser:
   http://127.0.0.1:5000/

---

## 🧠 Learning Outcomes
- Understanding SQL Injection attacks
- Writing vulnerable vs secure queries
- Using parameterized queries
- Implementing password hashing
- Basic web security practices

---

## ⚠️ Disclaimer
This project is for educational purposes only. Do not use these techniques on real systems without permission.