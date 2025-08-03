# 🧠 Smart CLI Assistant (Python)

A modular and interactive **Command Line Interface (CLI) Assistant** built in Python. It performs useful daily tasks via a terminal-based interface.

### ✅ Features

- 📅 View current date & time  
- 📓 Create, read, and manage notes  
- ✅ Maintain a to-do task list  
- 🌤️ Get real-time weather updates  
- 🗞️ Fetch latest news headlines (US only)  
- 😂 Hear a random joke  
- 📧 Send emails using Gmail automation  
- 🌐 Open any website via CLI  

---

## 🗂️ Folder Structure

```
Smart-CLI-Assistant/
│
├── main.py                # Main assistant launcher
├── modules/               # Contains all functional modules
│   ├── date_time.py
│   ├── notes.py
│   ├── todo.py
│   ├── weather.py
│   ├── news.py
│   ├── email_send.py
│   ├── fun_utils.py       # Jokes and utility features
│
├── notes.json             # Auto-generated notes data (same folder as main.py)
├── todo.json              # Auto-generated todo data (same folder as main.py)
└── README.md              # Project guide
```

---

## 🚀 How to Run

1. **Install required library**
   ```bash
   pip install requests
   ```

2. **Launch assistant**
   ```bash
   python main.py
   ```

---

## 🔐 Email Setup

If you want to use the Gmail feature:

1. Turn on **2-Step Verification** for your Gmail.
2. Generate a **Gmail App Password**.
3. Use that password in the assistant when sending emails (never use your actual password).

---

## 📌 Notes & To-Do Storage

- Notes and tasks are stored in `notes.json` and `todo.json`, created automatically in the same folder as `main.py`.
- You don’t need to manually create or manage these files.

---

## 📦 Future Add-ons (optional)

- Add colors and themes using `colorama` or `rich`
- Enable voice input/output
- Support for more countries in the news module

---

## 👨‍💻 Built Using

- Python 3
- `requests`, `json`, `datetime`, `webbrowser`, `smtplib`
