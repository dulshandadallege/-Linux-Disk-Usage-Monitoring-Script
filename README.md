# ✅ What it does:

* Checks disk space usage on Linux servers.
* Alerts if disk usage exceeds a defined threshold.
* Can be integrated with Slack, email, or monitoring tools.
  
# How to Use:
### 1. Install required dependencies (if needed):
```
pip install smtplib
```
### 2. Modify configuration:
* Set the THRESHOLD (e.g., 80 for 80% usage).
* Update SMTP settings with your email provider.
* Set ALERT_EMAIL to receive notifications.

### 3. Run the script manually or as a cron job:
```
python disk_monitor.py
```
Or schedule it with `crontab -e:`
```
*/30 * * * * /usr/bin/python3 /path/to/disk_monitor.py
```
# Why is this Useful for DevOps?
* Prevents server crashes due to full disks.
* Automates monitoring instead of manual checks.
* Can integrate with Slack, PagerDuty, or Prometheus for better alerting.