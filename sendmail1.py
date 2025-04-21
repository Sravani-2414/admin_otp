import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
 
def send_message1(mail,name,fee):
 
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
 
    username = "sravanichowdary8262@gmail.com"
    password = "eevo kobt grqh zylz"
 
    from_email = "sravanichowdary8262@gmail.com"
    subject = "Fee Remainder"
    body = f"Dear {name},\nPlease make sure to pay the remaining {40000-fee} as soon as possible."
 
    msg = MIMEMultipart()
    msg["From"] = from_email
    msg["To"] = mail
    msg["Subject"] = subject
    msg.attach(MIMEText(body,"plain"))
 
    server = smtplib.SMTP(smtp_server,smtp_port)
    server.starttls()
    server.login(username,password)
    server.send_message(msg)
    server.quit()
    print(f"Email Sent to {mail} is Success !")

