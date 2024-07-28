import pywhatkit as kit
import schedule
import time

# Function to send WhatsApp message
def send_whatsapp_message():
    phone_number = '+233271237965'  # Replace with the receiver's phone number
    message = 'Please ensure. You always study. Its for your benefit.\n\nWhen last you study'
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
schedule_whatsapp_message(20, 30)  # Example: 3:30 PM
