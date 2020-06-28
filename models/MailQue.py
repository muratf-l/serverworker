import datetime
from mongoengine import *


class MailQue(Document):
    meta = {'collection': 'SMailQue'}

    acc_id = StringField()

    mail_subject = StringField()

    mail_body = StringField()

    from_name = StringField()

    from_address = StringField()

    to_address = StringField()

    is_send = BooleanField()

    date_created = DateTimeField(default=datetime.datetime.utcnow)

    date_send = DateTimeField()

    send_error = BooleanField()

    send_detail = StringField()

    @staticmethod
    def add_quee(acc_id, to, subject, body):
        from app.AppCore import instance

        mail = MailQue()
        mail.acc_id = acc_id
        mail.is_send = False
        mail.to_address = to
        mail.mail_body = body
        mail.mail_subject = subject
        mail.from_address = instance.config["MAIL_SENDER_MAIL"]

        import email.utils
        mail.from_name = email.utils.formataddr(
            (instance.config["MAIL_SENDER"], instance.config["MAIL_SENDER_MAIL"]))
        mail.save()
