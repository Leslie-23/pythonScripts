import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time

# Function to send email
def send_email():
    # Email credentials
    # sender_email = 'your_email@example.com'
    # receiver_email = 'receiver_email@example.com'
    # password = 'your_password'
    
    sender_email = "leslieajayi27@gmail.com"
    receiver_email = "leslieajayi27@gmail.com"
    password = "123456Seven88"  # Use an app password for Gmail

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = 'Automated Email'

    body = 'This is an automated email sent at a scheduled time.'
    msg.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server and send the email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            text = msg.as_string()
            server.sendmail(sender_email, receiver_email, text)
            print('Email sent successfully!')
    except Exception as e:
        print(f'Error: {e}')

# Schedule the email to be sent at a specific time
def schedule_email(hour, minute):
    schedule.every().day.at(f"{hour:02d}:{minute:02d}").do(send_email)
    
    while True:
        schedule.run_pending()
        time.sleep(60)  # Wait for one minute

# Call the function with your desired time
schedule_email(20, 14)  # Example: 3:30 PM
