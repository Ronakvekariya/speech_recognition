# import keys
# import os
# from twilio.rest import Client

# client = Client(keys.account_SID, keys.auth_token) 


# demo_message = "sending demo message from the audio & image classification part"
# message = client.messages.create(body=f"{demo_message}",from_="+1234567890",to="+19876543210")

# print(message.sid)
#uoxw mend agrt npwq

import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os


print(os.getcwd())

try:
    # Email credentials
    sender_email = "65ronakvekariya@gmail.com"
    receiver_email = "poojavekariya2018@gmail.com"
    password = "uoxw mend agrt npwq"

    # Create the email headers
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = "Testing the email component"

    # Body of the email
    body = "This email contains an image/audio attachment."
    message.attach(MIMEText(body, 'plain'))

    # File to be sent (image or audio)
    filename = "./speech_recognition/L1_Indiviual_Components/SMS/1_0002.jpg"  # Replace with your file name and extension
    attachment = open(filename, "rb")

    # Instance of MIMEBase and encode the file
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(filename)}')

    # Attach the file to the email
    message.attach(part)

    # Close the file
    attachment.close()

    # Connect to Gmail's SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)

    # Send the email
    text = message.as_string()
    server.sendmail(sender_email, receiver_email, text)

    # Disconnect from the server
    server.quit()
except Exception as e:
    print(e)