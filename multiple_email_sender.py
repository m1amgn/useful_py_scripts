# Bulk Email Sender

import smtplib as smtp
from email.message import EmailMessage

emails = ["test1@email.com", "test2@email.com"]
Email = "myemail@test.com"
Pass = "mypassword"E_msg = EmailMessage()

E_msg['Subject'] = "Test Email"
E_msg['From'] = Email
E_msg['To'] = emails
E_msg.set_content("This is a test email")

with smtp.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(Email, Pass)
    smtp.send_message(E_msg)
