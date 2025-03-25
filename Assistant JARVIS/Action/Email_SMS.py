from Body.Advance_speak import speak
from Body.Speech_to_Text import listen
import smtplib
import requests
from twilio.rest import Client

# Function to send email (example using Gmail SMTP)
def send_email():
    try:
        # Replace with your email credentials
        gmail_user = 'your_email@gmail.com'
        gmail_password = 'your_password'
        
        # Establish a secure session with Gmail's outgoing SMTP server using your gmail account
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        
        # Customize email content
        subject = "Test Email from Voice Commands"
        body = "This is a test email sent from a Python script using voice commands."
        message = f"Subject: {subject}\n\n{body}"
        
        # Replace with recipient email address
        recipient = "recipient_email@example.com"
        server.sendmail(gmail_user, recipient, message)
        server.close()
        
        speak("Email sent successfully!")
    except Exception as e:
        speak(f"Error sending email: {e}")

# Function to send SMS (example using Twilio API)
def send_sms(command):
    try:
        # Twilio account SID and auth token
        account_sid = 'your_account_sid'
        auth_token = 'your_auth_token'
        
        client = Client(account_sid, auth_token)
        
        # Extract recipient and message from command
        recipient = command.split("send sms to ")[1].split(" message ")[0]
        message_body = command.split(" message ")[1]
        
        # Replace with your Twilio phone number
        from_number = 'your_twilio_number'
        
        # Send SMS using Twilio
        message = client.messages.create(
            body=message_body,
            from_=from_number,
            to=recipient
        )
        
        speak(f"SMS sent successfully to {recipient}")
    except Exception as e:
        speak(f"Error sending SMS: {e}")

def Email_Sms_Action():
        if "send email" in command:
            send_email()
        elif "send sms" in command:
            send_sms(command)

        else:
            speak(f"Command '{command}' not recognized.")

if __name__ == "__main__":
    while True:
        command = listen()
        
        if "exit" in command:
            speak("Exiting...")
            break
        
        if command:
            Email_Sms_Action(command)