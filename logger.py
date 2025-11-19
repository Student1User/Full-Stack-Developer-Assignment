from datetime import datetime

LOG_FILE = "sms_log.txt"

def log_success(number):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} - SUCCESS - {number}\n")

def log_failure(number, error):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} - FAILURE - {number} - {error}\n")
