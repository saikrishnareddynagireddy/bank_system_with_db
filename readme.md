# 🏦 Secure Banking System (Python + SQLite)

## 📌 Project Overview

This project is a console-based Secure Banking System developed using Python and SQLite.  
It allows users to create accounts, authenticate using passwords, and perform banking operations such as deposit, withdrawal, and balance inquiry.

The system ensures secure data handling using password hashing and parameterized SQL queries.

---

## 🚀 Features

- 🔐 Secure Password Authentication (SHA-256 Hashing)
- 💾 SQLite Database Integration
- 🏦 Create New Account
- 💰 Deposit Money
- 💸 Withdraw Money
- 📊 Check Account Balance
- 🛡 Protection Against SQL Injection
- 🗂 Persistent Data Storage (`bank.db`)

---

## 🛠 Technologies Used

- Python 3
- SQLite (`sqlite3`)
- Hashlib (for password encryption)

---

## 🗄 Database Structure

### Table: `accounts`

| Column Name      | Data Type | Description |
|------------------|----------|-------------|
| account_number   | INTEGER (Primary Key, Auto Increment) | Unique account ID |
| name             | TEXT     | Account holder name |
| password         | TEXT     | Hashed password |
| balance          | REAL     | Current account balance |

---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/saikrishnareddynagireddy/bank_system_with_db.git
```

### 2️⃣ Navigate to Project Folder

```bash
cd banking-system
```

### 3️⃣ Run the Program

```bash
python main.py
```

> The database file `bank.db` will be automatically created on first run.

---

## 🔐 Security Implementation

- Passwords are stored using SHA-256 hashing.
- SQL queries use parameterized statements to prevent SQL injection.
- Authentication is required before performing transactions.

---

## 📚 Learning Outcomes

Through this project, I learned:

- Database connectivity in Python
- Writing SQL queries (INSERT, SELECT, UPDATE)
- Implementing authentication logic
- Secure password handling
- Backend development fundamentals

---

## 🔮 Future Improvements

- Add transaction history tracking
- Implement session-based login
- Add admin dashboard
- Convert to MySQL (production-level database)
- Build a web version using Flask or Django

---

## 👨‍💻 Author

Sai Krishna Reddy  
Aspiring Backend & Data Science Developer 🚀