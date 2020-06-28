import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_mail(body, subject, to, from_name, from_mail):
    from app.AppCore import instance

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = from_name
    msg['To'] = to

    part2 = MIMEText(body, 'html')
    msg.attach(part2)

    try:
        server = smtplib.SMTP(instance.config["MAIL_SERVER"], instance.config["MAIL_SERVER_PORT"])
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(instance.config["MAIL_USER_NAME"], instance.config["MAIL_USER_PASS"])
        server.sendmail(from_mail, to.split(','), msg.as_string())
        server.close()

    except Exception as e:
        print("Error: ", e)
        return False, str(e)
    else:
        print("Email sent!")
        return True, None
