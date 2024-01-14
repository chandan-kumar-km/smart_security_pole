from email.message import EmailMessage
import ssl
import smtplib
def mail():
    email_sender = 'chandanchandan51218@gmail.com'
    email_password ='mieldjlbptbtldjp'

    email_receiver = 'chandankm51218@gmail.com'
    subject = "alert for drone"
    body=""" drone detected"""
    em = EmailMessage()
    em['From'] = email_sender
    em['to'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_receiver,em.as_string())