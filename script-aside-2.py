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
