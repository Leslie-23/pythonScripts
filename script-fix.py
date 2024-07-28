import schedule
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_reminder_email():
    try:
        # Email configuration
        sender_email = "seunpaul003@gmail.com"
        receiver_email = "leslieajayi27@gmail.com"
        password = "123456Seven88"  # Use an app password for Gmail

        # Create message
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = "Daily Reminder"

        # Email body
        body = "Good morning! This is your daily reminder. Have a great day!"
        message.attach(MIMEText(body, "plain"))

        # Send email
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            print("Reminder email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Schedule the job
schedule.every().day.at("19:58").do(send_reminder_email)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
