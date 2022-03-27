import ssl
import smtplib
def send_notification(days_to_expire):
    smtp_port = 587
    smtp_server = "smtp.mwam.com"
    sender_email = "operations@mwam.com"
    receiver_email = "webmaster@mwam.com"
    password = "smptPassword"
    if days_to_expire== 1:
        days = "1 day"
    else:
        days = str(days_to_expire) + " days"
        
    message = """\
        Subject: Certificate Expiration
        The TLS Certificate for mwam site expires in {days}"""

    email_context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls(context = email_context)
        server.login(sender_email, password)
        server.sendmail(sender_email, 
                        receiver_email, 
                        message.format(days = days))