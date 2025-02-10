# Micro API Authentication

## 📖 Description
This project was created to be a micro API for authentication and session token generation.

## 📌 Goal
The goal was to practice with the FastAPI, Pydantic and Uvicorn libraries, working on session token concepts.

---

## 💻 Technologies
- **Python**: Version 3.12.3 

## Libraries
- **FastAPI**: Version 0.115.8
- **Pydantic**: Version 2.10.6
- **Uvicorn**: Version 0.34.0

---

## ✨ Features
- Register user: Validates and registers the user by saving it to the database
- Login user: Authenticates the user and generates the session token

---

## 🛠 Installation

### ✅ Requirements
1. **Python**: Make sure Python is installed on your system. https://www.python.org/downloads/
2. **Git**: Install Git to clone the repository. https://git-scm.com/downloads

### 🔄 Clone the Repository
Open your terminal (Bash, PowerShell, or CMD) and run the following command:
```bash
git clone https://github.com/juniorferreira23/Micro_Api_Authentication.git
```

### 🌐 Creating a Virtual Environment
```bash
python3 -m venv venv
```

### Activate Virtual Environment
Windows
```cmd
.\venv\Scripts\activate.ps1
```

Linux
```bash
source venv/bin/activate
```

### 📦 Installing Dependencies
In the virtual environment, install the required libraries:
```bash
pip install -r requirements.txt
```

### ▶️ Running the Code
To run the program directly, use:
```bash
uvicorn main:app --reload
```

### Swagger Endpoint Documentation
Access the links below to view the API endpoints:
http://localhost:8000/docs