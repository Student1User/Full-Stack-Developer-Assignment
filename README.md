SMS Automation System (Python + ADB + Scrcpy)

## Overview
This project automates sending SMS messages from an Android device using:
- **ADB (Android Debug Bridge)**
- **Scrcpy** (free screen mirroring tool)
- **PyAutoGUI** for UI automation
- **CSV contact lists**
- **Python logging**

This solution is fully free and demonstrates real automation skills suitable for professional environments.

---

## Features
✅ Reads phone numbers from `contacts.csv`  
✅ Opens Scrcpy automatically  
✅ Sends predefined SMS messages via Truecaller  
✅ Logs success/failure with timestamps  
✅ Uses stable ADB communication  
✅ All tools are free and open-source  

---

## Project Structure
sms-notifier/
│── contacts.csv
│── main.py
│── automation.py
│── logger.py
│── requirements.txt
│── README.md
│── sms_log.txt (generated automatically)

yaml
Copy code

---

## Installation (Windows + VS Code + PowerShell)

### 1. Install platform-tools (ADB)
Download from Google → extract → run:
adb devices

shell
Copy code

### 2. Install Scrcpy
Download from GitHub → extract → note the folder path.

### 3. Create virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt

yaml
Copy code

---

## Running the Script
1. Connect your phone with USB debugging enabled  
2. Open VS Code → Terminal → run:

python main.py

yaml
Copy code

3. Scrcpy launches  
4. The script sends SMS to all numbers in the CSV  
5. Logs appear in `sms_log.txt`

---

## Security Overview
- No data is stored online  
- Messages are sent directly on the phone  
- No external API is used  
- The CSV file should be stored securely  
- The user must trust the connected phone (USB debugging)

---


