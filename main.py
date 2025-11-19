import pandas as pd
import pyautogui
import time
from logger import log_success, log_failure

MESSAGE = "Hello! This is an automated message from my SMS Notification System."

# Time settings
SEARCH_DELAY = 1  # wait after clicking search bar
TYPE_DELAY = 0.05
MESSAGE_DELAY = 1  # wait after sending

def send_bulk_messages(csv_path, message):
    df = pd.read_csv(csv_path)
    
    for _, row in df.iterrows():
        number = str(row["number"])
        try:
            print(f"Sending message to {number}...")
            
            # Step 1: Open search in Truecaller
            pyautogui.hotkey('ctrl', 'f')  # typical shortcut to focus search bar, adjust if needed
            time.sleep(SEARCH_DELAY)
            
            # Step 2: Type the number
            pyautogui.typewrite(number, interval=TYPE_DELAY)
            time.sleep(SEARCH_DELAY)
            
            # Step 3: Press Enter to open chat
            pyautogui.press('enter')
            time.sleep(SEARCH_DELAY)
            
            # Step 4: Type the message
            pyautogui.typewrite(message, interval=TYPE_DELAY)
            pyautogui.press('enter')
            time.sleep(MESSAGE_DELAY)
            
            log_success(number)
      
            
        except Exception as e:
            log_failure(number, str(e))
    
    print("All messages sent! Check sms_log.txt for details.")

if __name__ == "__main__":
    print("Make sure Truecaller SMS is open in the scrcpy window...")
    time.sleep(5)  # time to switch to scrcpy manually
    send_bulk_messages("contacts.csv", MESSAGE)
