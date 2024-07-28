# Messaging Automation Scripts

This repository contains Python scripts for automating messaging through various channels: email, phone (SMS), and WhatsApp. Each script is designed to send messages at a scheduled time.

## Table of Contents

- [1. Email Automation](#1-email-automation)
- [2. SMS Automation](#2-sms-automation)
- [3. WhatsApp Automation](#3-whatsapp-automation)

---

## 1. Email Automation

This script sends an email at a specified time using the `smtplib` and `schedule` libraries.

### Requirements

- Python 3.x
- `schedule` library

Install the required library using:
```bash
pip install schedule
```

### Script

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time

# Function to send email
def send_email():
    # Email credentials
    sender_email = 'your_email@example.com'
    receiver_email = 'receiver_email@example.com'
    password = 'your_password'

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = 'Automated Email'

    body = 'This is an automated email sent at a scheduled time.'
    msg.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server and send the email
    try:
        with smtplib.SMTP('smtp.example.com', 587) as server:
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
schedule_email(15, 30)  # Example: 3:30 PM
```

---

## 2. SMS Automation

This script sends an SMS using the Twilio API.

### Requirements

- Python 3.x
- `twilio` library

Install the required library using:
```bash
pip install twilio
```

### Script

```python
from twilio.rest import Client
import schedule
import time

# Twilio credentials
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

# Function to send SMS
def send_sms():
    message = client.messages.create(
        body='Hello! This is an automated SMS.',
        from_='+your_twilio_number',  # Replace with your Twilio phone number
        to='+1234567890'  # Replace with the receiver's phone number
    )
    print(f'SMS sent successfully with SID: {message.sid}')

# Schedule the SMS to be sent at a specific time
def schedule_sms(hour, minute):
    schedule.every().day.at(f"{hour:02d}:{minute:02d}").do(send_sms)
    
    while True:
        schedule.run_pending()
        time.sleep(60)  # Wait for one minute

# Call the function with your desired time
schedule_sms(15, 30)  # Example: 3:30 PM
```

---

## 3. WhatsApp Automation

This script sends a WhatsApp message using the `pywhatkit` library.

### Requirements

- Python 3.x
- `pywhatkit` library

Install the required library using:
```bash
pip install pywhatkit
```

### Script

```python
import pywhatkit as kit
import schedule
import time

# Function to send WhatsApp message
def send_whatsapp_message():
    phone_number = '+1234567890'  # Replace with the receiver's phone number
    message = 'Hello! This is an automated message.'
    # Schedule the message to be sent 1 minute from now
    kit.sendwhatmsg(phone_number, message, time_hour, time_minute)

# Schedule the message to be sent at a specific time
def schedule_whatsapp_message(hour, minute):
    global time_hour, time_minute
    time_hour = hour
    time_minute = minute
    schedule.every().day.at(f"{hour:02d}:{minute:02d}").do(send_whatsapp_message)
    
    while True:
        schedule.run_pending()
        time.sleep(60)  # Wait for one minute

# Call the function with your desired time
schedule_whatsapp_message(15, 30)  # Example: 3:30 PM
```

---

## Notes

- **Email Automation:**
  - Replace placeholders such as `your_email@example.com`, `receiver_email@example.com`, and `your_password` with your actual email credentials and details.
  - Ensure your SMTP server settings are correct for sending emails.

- **SMS Automation:**
  - Replace `your_account_sid`, `your_auth_token`, and `+your_twilio_number` with your Twilio credentials and phone number.
  - Make sure the phone number format is correct.

- **WhatsApp Automation:**
  - Ensure you are logged into WhatsApp Web in your default web browser when the script runs.
  - Replace `+1234567890` with the receiver's phone number.

Feel free to modify the scripts as needed to fit your use case.

---
