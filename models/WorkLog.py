from mongoengine import *
import datetime


class WorkLog(Document):
    meta = {'collection': 'SWorkLogs'}

    _id = ObjectIdField()

    date_created = DateTimeField(default=datetime.datetime.utcnow)

    r_code = IntField()

    r_content = StringField()
