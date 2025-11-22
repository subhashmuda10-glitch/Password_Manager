# 🔐 Password Manager (Python)

A simple desktop Password Manager application built using **Python** and **Tkinter**.

This app allows you to:
- Generate secure random passwords 🔑  
- Save website credentials (website, email, password)
- Search & retrieve saved passwords instantly
- Store data safely in a JSON file


---

## 🚀 Features

### ✔ 1. Secure Password Generator
- Generates strong passwords with:
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Symbols
- Fully random, unique every time

### ✔ 2. Save Credentials
- Saves:
  - Website
  - Email / Username
  - Password
- Stores data in **data_file.json**

### ✔ 3. Search Existing Credentials
- Enter the website name
- Instantly retrieve:
  - Email
  - Password
- If not found → shows alert message

---

## 📁 Tech Stack

| Component | Technology |
|----------|------------|
| Programming Language | Python |
| GUI Toolkit | Tkinter |
| Data Storage | JSON |
| Modules Used | tkinter, random, json |

---

## 🧩 Project Structure

Password_Manager/
│
├── main.py
├── data_file.json
├── logo.png
├── text_file.txt
└── README.md


## 🖥 How to Run

### 1️⃣ Install Python (3.8+ recommended)

Check version:
```bash
python --version
2️⃣ Clone this project
bash
Copy code
git clone https://github.com/<your-username>/Password_Manager.git
3️⃣ Run it
bash
Copy code
python main.py
📷 App Preview

<img width="509" height="436" alt="image" src="https://github.com/user-attachments/assets/5dc6b416-5177-47ae-89f8-0b7de3a81d95" />


🗄 Data Storage Format (JSON)
Example data_file.json:

json
Copy code
{
  "google.com": {
    "Email": "example@gmail.com",
    "Password": "Agh76!gbHB@"
  }
}
🔮 Future Enhancements (Optional)
Encrypt stored passwords

Add login authentication

Export passwords

Cloud sync

Dark mode theme

⭐ Author
Subhash Chandra Bose
(Designed & developed using Python)
