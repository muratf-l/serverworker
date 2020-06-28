import datetime
from mongoengine import *

from app.helpers.mailUtil import send_mail


def job_mail_quee():
    from app.AppCore import instance
    print("job_mail_quee")

    from models.MailQue import MailQue

    maillist = MailQue.objects(is_send=False).limit(instance.config["JOB_MAIL_DB_LIMIT"])

    for row in maillist:
        res = send_mail(
            row.mail_body,
            row.mail_subject,
            row.to_address,
            row.from_name,
            row.from_address
        )

        row.is_send = True

        if res[0] is False:
            row.send_error = True
            row.send_detail = res[1]
        else:
            row.send_error = False
            row.send_detail = ""

        row.date_send = datetime.datetime.utcnow
        row.save()
