from email.mime.text import MIMEText
import smtplib

def send_email(email, name, subject, message):
    from_email = "" # your email address
    from_password = ""  # put email password in here, only do this locally do not push with this for security reasons
                                   # for deployment we need to set environment vaiables for above security reasons
    to_email = from_email

    subject = subject
    message = f"<b>Name:</b> {name}<br><b>Email:</b> {email}<br><br>{message}"
    msg = MIMEText(message, 'html')

    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    email = smtplib.SMTP("smtp.live.com", 587)  # if you are sending from gmail change this to smtp.gmail.com
    email.ehlo()
    email.starttls()
    email.login(from_email, from_password)
    email.send_message(msg)
