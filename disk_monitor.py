import shutil
import smtplib
from email.mime.text import MIMEText

# Configuration
THRESHOLD = 80  # Alert if disk usage exceeds this percentage
ALERT_EMAIL = "admin@example.com"
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
SMTP_USER = "your_email@example.com"
SMTP_PASSWORD = "your_password"

def check_disk_usage():
    """Check disk usage and return the percentage used."""
    total, used, free = shutil.disk_usage("/")
    percent_used = (used / total) * 100
    return percent_used

def send_alert(usage):
    """Send an email alert if disk usage exceeds threshold."""
    subject = "🚨 Disk Usage Alert!"
    body = f"Warning: Disk usage is at {usage:.2f}%.\nPlease investigate and free up space if necessary."
    
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SMTP_USER
    msg["To"] = ALERT_EMAIL
    
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.sendmail(SMTP_USER, ALERT_EMAIL, msg.as_string())
        print("✅ Alert email sent successfully.")
    except Exception as e:
        print(f"❌ Failed to send alert email: {e}")

if __name__ == "__main__":
    disk_usage = check_disk_usage()
    print(f"📊 Current Disk Usage: {disk_usage:.2f}%")
    
    if disk_usage > THRESHOLD:
        print("⚠️ Disk usage exceeded threshold! Sending alert...")
        send_alert(disk_usage)
    else:
        print("✅ Disk usage is within safe limits.")
