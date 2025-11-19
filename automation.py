import subprocess
import time
import pyautogui
import pandas as pd
from logger import log_success, log_failure

SCRCPY_PATH = r"C:\Users\Emmanuel Jesse\Downloads\scrcpy-win64-v3.3.3\scrcpy-win64-v3.3.3\scrcpy.exe"

def start_scrcpy():
    try:
        subprocess.Popen([SCRCPY_PATH])
        print("Starting scrcpy...")
        time.sleep(5)  # Wait for phone screen to appear
    except Exception as e:
        print("Failed to start scrcpy:", e)

def send_sms_via_google_messages(number, message):
    """
    Automates SMS sending via Google Messages using scrcpy + PyAutoGUI
    """
    try:
        # Step 1: Click search/start chat
        # Coordinates must match your screen. Adjust x, y
        pyautogui.click(x=200, y=150)  # example: search bar
        time.sleep(1)
        
        # Step 2: Type number and press Enter
        pyautogui.typewrite(number, interval=0.05)
        time.sleep(0.5)
        pyautogui.press("enter")
        time.sleep(1)
        
        # Step 3: Click message box
        pyautogui.click(x=500, y=1200)  # example: message input box
        time.sleep(0.5)
        
        # Step 4: Type message and send
        pyautogui.typewrite(message, interval=0.05)
        pyautogui.press("enter")
        time.sleep(1)
        
        log_success(number)
    except Exception as e:
        log_failure(number, str(e))

def send_bulk_messages(csv_path, message):
    df = pd.read_csv(csv_path)
    for _, row in df.iterrows():
        number = str(row["number"])
        print(f"Sending to {number}...")
        send_sms_via_google_messages(number, message)
        time.sleep(1)

